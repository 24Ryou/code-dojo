import os
from db import SQLiteDB
import temp
import json
import requests
import shutil
import re

def url_to_json(url: str) -> dict:
    """
    This function takes a URL, sends a GET request to it, and returns the JSON data if the response
    status code is 200, otherwise it prints an error message.

    :param url: The URL of the resource that we want to retrieve and convert to JSON format
    :type url: str
    :return: a dictionary object containing the data obtained from the specified URL. If the response
    status code is not 200, an error message is printed and nothing is returned.
    """
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        write_to_json(data, f"resource/{data['slug']}.json")  # optional
        return data
    else:
        print("Error: ", response.status_code)


def write_to_json(data: dict, filename: str) -> bool:
    """
    This function writes a dictionary to a JSON file and returns True if successful, False otherwise.

    :param data: A dictionary containing the data to be written to the JSON file
    :type data: dict
    :param filename: The filename parameter is a string that represents the name of the file to which
    the data will be written in JSON format
    :type filename: str
    :return: a boolean value. If the data is successfully written to the JSON file, it returns True. If
    there is an IOError, indicating that the file could not be opened or written to, it returns False.
    """
    try:
        with open(filename, "w") as file:
            json.dump(data, file)
            return True
    except IOError:
        return False


def insert_kata(data: dict) -> bool:
    """
    The function inserts data into a SQLite database table called "katas".

    :param data: A dictionary containing the data to be inserted into the "katas" table in a SQLite
    database
    :type data: dict
    :return: a boolean value.
    """
    sql = '''
  INSERT OR IGNORE INTO katas (uid, name, slug, url, rank, description, languages , solutions)
  VALUES (:uid, :name, :slug, :url, :rank, :description, :languages, :solutions)
  '''
    params = {
        "uid": data['id'],
        'name': data['name'],
        'slug': data['slug'],
        'url': data['url'],
        'rank': data['rank']['name'],
        'description': data['description'],
        'languages': " - ".join(data['languages']),
        'solutions': "none"
    }
    db = SQLiteDB()
    return db.execute_query(sql, params)


def insert_language(language_data: dict) -> bool:
    """
    The function `insert_language` inserts language data into a SQLite database table.

    :param language_data: A dictionary containing the data for the language to be inserted into the
    database. The keys of the dictionary represent the column names in the "languages" table, and the
    values represent the corresponding values to be inserted
    :type language_data: dict
    :return: a boolean value.
    """
    db = SQLiteDB()
    columns = list(language_data.keys())
    values = list(language_data.values())
    sql = "INSERT OR iGNORE INTO languages (%s) VALUES (%s);" % (
        ",".join(columns), ",".join(map(lambda x: f"'{x}'", values)))
    return db.execute_query(sql)


def add_solutions(uid: str, language: str) -> bool:
    db = SQLiteDB()
    value = db.fetch(f"select solutions from katas where katas.uid = '{uid}'")[0]
    if value != "none" and language not in value:
        language += " - " + language.strip()
    if copy_solution(uid, language):
        return db.execute_query("UPDATE katas SET solutions = ? WHERE uid = ?", (language.lower(), uid))
    else:
        return False


def sanitize_filename(filename):
    # Replace any characters that are not alphanumeric, a period, or a dash with an underscore
    return re.sub(r'[^\w.-]', '-', filename)


def copy_solution(uid: str, language: str) -> bool:
    db = SQLiteDB()
    language_row = db.fetch(
        "SELECT * FROM languages WHERE languages.name = '%s'" % language)
    app_path = language_row[2]
    dist_path = language_row[3]
    filetype = language_row[1]
    slug = db.fetch("SELECT slug FROM katas WHERE katas.uid = '%s'" % uid)
    slug = sanitize_filename(slug[0])
    try:
        if not os.path.exists(dist_path):
            os.makedirs(dist_path)
        shutil.copy(app_path, os.path.join(dist_path, "%s.%s" % (slug, filetype)))
        return True
    except OSError:
        return False

def get_uid_from_file(which_file : str) -> str:
    app_path = SQLiteDB().fetch(f"SELECT appPath FROM languages WHERE languages.name = '{which_file}';")[0]
    with open(app_path) as f:
        match = re.search(r"/kata/(\w+)", f.readline().split()[-1])
        if match:
            kata_id = match.group(1)
        return kata_id

def get_none_solutions():
    db = SQLiteDB()
    tuple_ = db.fetch("SELECT katas.uid , katas.name , katas.url FROM katas WHERE katas.solutions = 'none';" , None , True)
    if len(tuple_) == 0: 
        print("All katas are solved!")
        return
    for i , (uid , name , url) in enumerate(tuple_):
        print(f"{i} - {name} , {uid} , {url}")
    load()    

def save():
    languages = SQLiteDB().fetch("SELECT * FROM languages" , None , True)
    i = 0
    for language in languages:
        print("%s - %s" % (i , language[0].upper()))
        i += 1
    i = int(input("Enter your number: "))
    lang_name = languages[i][0]
    uid = get_uid_from_file(lang_name)
    slug = SQLiteDB().fetch(f"SELECT slug FROM katas WHERE katas.uid = '{uid}';")[0]
    add_solutions(uid , lang_name)
    print("%s solution added for %s" % (lang_name , slug))

def load():
    id = input("Please enter id: ")
    url = f"https://www.codewars.com/api/v1/code-challenges/{id}"
    data = url_to_json(url)
    print("Which language you want?")
    languages = SQLiteDB().fetch("SELECT * FROM languages" , None , True)
    languages = list(filter(lambda x: x[0] in data["languages"] , languages))
    i = 0
    for language in languages:
        print("%s - %s" % (i , language[0].upper()))
        i += 1
    i = int(input("Enter your number: "))
    with open(languages[i][2] , "w") as f:
        f.write(languages[i][-1].format(id))
    insert_kata(data)
    
def setup():
    db = SQLiteDB()
    db.execute_query(temp.CREATE_TABLE_KATAS)
    db.execute_query(temp.CREATE_TABLE_LANGUAGES)
    for langueage in temp.LANGUAGE_LIST:
        insert_language(langueage)
import sqlite3

class SQLiteDB:
  def __init__(self):
    self.conn = sqlite3.connect("codedojo.db")

  def __del__(self):
    self.conn.close()

  def execute_query(self, query, params=None) -> bool:
    """
    This function executes a SQL query with optional parameters and returns a boolean indicating success
    or failure.
    
    :param query: a string containing the SQL query to be executed
    :param params: params is a parameter that allows passing values to a SQL query as a tuple or a
    dictionary. It is used to prevent SQL injection attacks and to make the code more secure. If the
    query contains placeholders, the values in the params parameter will be substituted for the
    placeholders in the query. If the query
    :return: The function `execute_query` returns a boolean value. If the query is executed successfully
    and the changes are committed to the database, it returns `True`. If there is an error during
    execution, it returns `False`.
    """
    cursor = self.conn.cursor()
    try:
      if params:
        cursor.execute(query, params)
      else:
        cursor.execute(query)
      self.conn.commit()
      return True
    except sqlite3.Error as e:
      print(e)
      return False

  def fetch(self, query, params=None, fetch_all=False):
    """
    This function executes a SQL query with optional parameters and returns either a single row or all
    rows depending on the fetch_all parameter.
    
    :param query: The SQL query to be executed
    :param params: params is a parameter that allows you to pass values to a SQL query as parameters.
    This is useful for preventing SQL injection attacks and for making your code more modular and
    reusable. If you have a query with placeholders (e.g. "SELECT * FROM my_table WHERE id = %s"), you
    can
    :param fetch_all: A boolean parameter that determines whether to fetch all rows returned by the
    query or just the first row. If set to True, the function will return all rows as a list of tuples.
    If set to False, the function will return only the first row as a tuple, defaults to False
    (optional)
    :return: The fetch method returns either a single row or multiple rows (depending on the value of
    the fetch_all parameter) fetched from the database using the provided query and parameters.
    """
    cursor = self.conn.cursor()
    if params:
      cursor.execute(query, params)
    else:
      cursor.execute(query)

    if fetch_all:
      rows = cursor.fetchall()
      return rows
    else:
      row = cursor.fetchone()
      return row
CREATE_TABLE_KATAS = """
CREATE TABLE IF NOT EXISTS katas (
  uid NOT NULL PRIMARY KEY,
  name NOT NULL,
  slug NOT NULL,
  url NOT NULL,
  rank NOT NULL,
  description NOT NULL,
  languages NOT NULL,
  solutions NOT NULL
);
"""

# CREATE_TABLE_SOLUTIONS = """
# CREATE TABLE IF NOT EXISTS solutions (
#   uid NOT NULL,
#   language NOT NULL,
#   PRIMARY KEY (uid, language)
#   );
# """


CREATE_TABLE_LANGUAGES = """
CREATE TABLE IF NOT EXISTS languages (
  name NOT NULL PRIMARY KEY,
  filetype NOT NULL,
  appPath NOT NULL,
  solutionPath NOT NULL,
  test NOT NULL,
  text NOT NULL
  );
"""

PYTHON_START = """# https://www.codewars.com/kata/{}
# -------------------------------- SOLUTION ------------------------------- #
# ----------------------------------- TEST ----------------------------------- #
import codewars_test as test
"""

LANGUAGE_LIST = [
  {
  "name" : "python",
  "filetype" : "py",
  "appPath" : "app/kata.py",
  "solutionPath" : "dist/python",
  "test" : "https://docs.codewars.com/languages/python",
  "text" : PYTHON_START
  }
]
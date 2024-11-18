import sqlite3

con = sqlite3.connect(':memory:')
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS users (
  id integer PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  email TEXT UNIQUE,
  pwd TEXT
);
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS notes (
  id integer PRIMARY KEY AUTOINCREMENT,
  header TEXT,
  content TEXT,
  user_id integer,
  FOREIGN KEY (`user_id`) REFERENCES users (id)
);
''')

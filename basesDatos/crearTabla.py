import sqlite3

conn = sqlite3.connect('alumnos')
cursor = conn.cursor()

cursor.execute('''
          CREATE TABLE IF NOT EXISTS alumnos
          ([id] INTEGER PRIMARY KEY, 
          [name] TEXT NOT NULL)
          ''')

conn.commit()

cursor.close()
conn.close()

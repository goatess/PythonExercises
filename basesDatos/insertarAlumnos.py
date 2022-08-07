import sqlite3

conn = sqlite3.connect('alumnos')
cursor = conn.cursor()

cursor.execute('''
          INSERT INTO alumnos (id, name)

                VALUES
                (1,'Ana'),
                (2,'Juan'),
                (3,'Paco'),
                (4,'Sara'),
                (5,'Pepe')
          ''')

conn.commit()

cursor.close()
conn.close()

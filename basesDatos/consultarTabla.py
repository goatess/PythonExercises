import sqlite3
import pandas as pd

conn = sqlite3.connect('alumnos')
cursor = conn.cursor()

cursor.execute('SELECT * FROM alumnos')

dataframe = pd.DataFrame(cursor.fetchall(), columns=['id','name'])
print(dataframe)

cursor.close()
conn.close()

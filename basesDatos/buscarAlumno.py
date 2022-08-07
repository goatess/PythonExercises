import sqlite3
import pandas as pd


def searchStudent(name):
    conn = sqlite3.connect('alumnos')
    cursor = conn.cursor()
    
    query = f'SELECT * FROM alumnos WHERE name = "{name}"'
    rows = cursor.execute(query)
    dataframe = pd.DataFrame(rows.fetchall(), columns=['id','name'])
    print(dataframe) 
    
    cursor.close()
    conn.close()

def main():
    name = input("Nombre del alumno: ")
    searchStudent(name)
    
if __name__ == '__main__':
    main()

    



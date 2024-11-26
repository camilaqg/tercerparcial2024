import time 
import sqlite3 as sql 

def createDB():
    conn = sql.connect("autoconocimiento.db")
    print("Base de datos autoconocimiento creada")
    conn.commit()
    conn.close()
    
def createTabe():
    conn = sql.connect("autoconocimiento.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE experience_motivations (
    motivation_id INTEGER PRIMARY KEY AUTOINCREMENT,
    experience_id INTEGER,
    expected_impact TEXT,
    motivation_level INTEGER,
    target_date DATE,
    FOREIGN KEY (experience_id) REFERENCES growth_experiences(growth_id)
);              
    """)
    print("Tabla creada")
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    createDB()
    createTabe()
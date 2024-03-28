import sqlite3

conn = sqlite3.connect('myTestDB')

c = conn.cursor()

c.execute("""CREATE TABLE stats(
            name TEXT,
            kills INTEGER,
            assists INTEGER,
            deaths INTEGER
)""")

c.execute("""INSERT INTO stats VALUES
            ('Tanner', '20', 2, 10)
        """)
conn.commit()
conn.close()
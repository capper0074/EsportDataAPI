import pyodbc

def connect_to_database():
    server = 'temp-4sem-sqlserver.database.windows.net'
    database = 'temp-4sem-sqldb'
    username = 'CasperJensen'
    password = 'Casper0098'
    driver= '{ODBC Driver 17 for SQL Server}'

    try:
        conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        print("Forbindelse oprettet til databasen, godt gået Kasper er stolt af dig.")
        return conn
    except pyodbc.Error as e:
        print("Fejl ved oprettelse af forbindelse til databasen:", e)
        return None


# Test forbindelse
conn = connect_to_database()
if conn:
    conn.close()
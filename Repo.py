import pyodbc


def connect_to_database():
    # Erstat værdierne i connection_string med dine egne
    connection_string = 'DRIVER={SQL Server};SERVER=server_name;DATABASE=database_name;UID=username;PWD=password'

    try:
        # Opret forbindelse til databasen
        conn = pyodbc.connect(connection_string)
        print("Forbindelse oprettet til databasen.")
        return conn
    except pyodbc.Error as e:
        print("Fejl ved oprettelse af forbindelse til databasen:", e)
        return None


# Test forbindelse
conn = connect_to_database()
if conn:
    conn.close()
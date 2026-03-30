# import psycopg2

# # Connect to the PostgreSQL server
# try:
#     connection = psycopg2.connect(
#         user="sonar",  # your postgres username
#         password="sonar",  # your postgres password
#         host="localhost",  # server hosting the database
#         port="5432"  # default port
#     )

#     # Create a cursor object
#     cursor = connection.cursor()

#     # Execute the SQL query to get all databases
#     cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
    
#     # Fetch all results
#     databases = cursor.fetchall()

#     # Print the list of databases
#     print("List of PostgreSQL Databases:")
#     for db in databases:
#         print(db[0])

# except Exception as e:
#     print(f"Error: {e}")

# finally:
#     # Close the cursor and the connection
#     if cursor:
#         cursor.close()
#     if connection:
#         connection.close()

import psycopg2
from psycopg2 import sql

def get_postgres_databases(host="localhost", port="5432", user="your_username", password="your_password"):
    """
    Connects to the PostgreSQL server and fetches all non-template database names.
    
    Returns:
        list of database names (str)
    """
    try:
        # Connect to the PostgreSQL server
        connection = psycopg2.connect(
            dbname="postgres",  # Connect to the default "postgres" database
            user=user,
            password=password,
            host=host,
            port=port
        )
        # Create a cursor object
        cursor = connection.cursor()

        # Execute the SQL query to get all databases
        cursor.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
        
        # Fetch all results
        databases = cursor.fetchall()

        # Return database names as a list of strings
        return [db[0] for db in databases]

    except Exception as e:
        print(f"Error: {e}")
        return []
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def print_database_tables(dbname, host="localhost", port="5432", user="your_username", password="your_password"):
    """
    Given a database name, this function connects to the database and prints a formatted list of all tables.
    
    Args:
        dbname: The name of the database
        host: The host of the PostgreSQL server
        port: The port of the PostgreSQL server
        user: The PostgreSQL username
        password: The PostgreSQL password
    """
    try:
        # Connect to the specified database
        connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Execute the SQL query to get all table names
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            ORDER BY table_name;
        """)

        # Fetch all results
        tables = cursor.fetchall()

        # Print formatted output
        print(f"\nTables in database '{dbname}':")
        if tables:
            print(f"{'Table Name':<30}")
            print("="*30)
            for table in tables:
                print(f"{table[0]:<30}")
        else:
            print("No tables found.")

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        # Close the cursor and the connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()


# Example usage
if __name__ == "__main__":
    databases = get_postgres_databases(user="sonar", password="sonar")

    if databases:
        print("List of PostgreSQL Databases:")
        for db in databases:
            print(db)
            # For each database, print its tables
            print_database_tables(db, user="sonar", password="sonar")
    else:
        print("No databases found or failed to connect.")

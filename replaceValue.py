import psycopg2
from psycopg2 import sql

# Database connection parameters
conn_params = {
    "dbname": "sonarqube",
    "user": "sonar",
    "password": "sonar",
    "host": "127.0.0.1",
    "port": "5432"
}

try:
    # Establish a connection to the database
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()

    # SQL command to update the value
    update_query = sql.SQL("UPDATE {table} SET {column} = %s WHERE {column} = %s").format(
        table=sql.Identifier('project_branches'),
        column=sql.Identifier('kee')
    )

    # Execute the command
    cursor.execute(update_query, ('someOtherUniqBranch', 'someUniqBranch'))
    conn.commit()

    print("Value updated successfully.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
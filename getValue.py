import psycopg2

# Database connection parameters
db_params = {
    "dbname": "sonar",
    "user": "sonar",
    "password": "sonar",
    "host": "172.30.0.143",
    "port": "5432"
}

# Function to find tables containing the value
def find_tables_with_value(value):
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_params)
    cur = conn.cursor()

    # Get the list of all tables and columns
    cur.execute("""
        SELECT table_name, column_name 
        FROM information_schema.columns 
        WHERE table_schema = 'public';
    """)

    tables_and_columns = cur.fetchall()
    print("tables_and_columns: ", tables_and_columns)

    # Result to store tables and columns where the value exists
    tables_with_value = []

    for table, column in tables_and_columns:
        # Formulate the query to search for the value
        query = f"""
            SELECT COUNT(*) 
            FROM "{table}" 
            WHERE "{column}"::TEXT = %s;
        """
        cur.execute(query, (value,))
        count = cur.fetchone()[0]

        # If the value is found in this column, store the result
        if count > 0:
            tables_with_value.append((table, column))

    # Close the cursor and connection
    cur.close()
    conn.close()

    return tables_with_value

# Replace 'your_value' with the value you're searching for
value_to_search = 'uniqProjBranch'

# Find tables and columns that contain the value
results = find_tables_with_value(value_to_search)

# Display results
if results:
    print("Found value in the following tables and columns:")
    for table, column in results:
        print(f"Table: {table}, Column: {column}")
else:
    print("No tables contain the value.")


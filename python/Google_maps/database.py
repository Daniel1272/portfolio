import psycopg2

# Database connection details
DATABASE_USER = 'user'
DATABASE_PASSWORD = 'password'
DATABASE_HOST = 'host'
DATABASE_PORT = 'port'
DATABASE_NAME = 'db_name'

# Create connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname=DATABASE_NAME,
    user=DATABASE_USER,
    password=DATABASE_PASSWORD,
    host=DATABASE_HOST,
    port=DATABASE_PORT
)

# Create a cursor object to interact with the database
cur = conn.cursor()


def add_to_database(phone_number, address, website):
    # Replace single quotes in the address to prevent SQL injection issues
    if address is not None:
        if "'" in address:
            address = address.replace("'", "''")

    # Create the SQL insert query
    insert_query = (f"INSERT INTO google_logistics1(phone_number, adress, website)"
                    f" VALUES ('{phone_number}','{address}','{website}')")
    try:
        # Execute the insert query
        cur.execute(insert_query)
        # Commit the transaction
        conn.commit()
        print("Data inserted successfully")
    except psycopg2.Error as e:
        # Print the error and rollback the transaction in case of an error
        print(f"Error: {e}")
        conn.rollback()

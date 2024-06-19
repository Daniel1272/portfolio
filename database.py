import psycopg2


DATABASE_USER = 'user'
DATABASE_PASSWORD = 'password'
DATABASE_HOST = 'host'
DATABASE_PORT = '5432'
DATABASE_NAME = 'db_name'

# Create connection
conn = psycopg2.connect(
    dbname=DATABASE_NAME,
    user=DATABASE_USER,
    password=DATABASE_PASSWORD,
    host=DATABASE_HOST,
    port=DATABASE_PORT
)

# create cursor
cur = conn.cursor()


def add_to_database(phone_number, address, website):

    if address is not None:
        if "'" in address:
            address = address.replace("'", "''")

    insert_query = (f"INSERT INTO google_logistics1(phone_number, adress, website)"
                    f" VALUES ('{phone_number}','{address}','{website}')")
    try:
        cur.execute(insert_query)
        conn.commit()
        print("Data inserted successfully")
    except psycopg2.Error as e:
        print(f"Error: {e}")
        conn.rollback()

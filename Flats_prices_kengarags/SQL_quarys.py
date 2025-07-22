import psycopg2

# Database connection details
DATABASE_USER = 'your_username'
DATABASE_PASSWORD = 'your_password'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5432'
DATABASE_NAME = 'flats_prices_riga'

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


def add_to_database(address, rooms, square_meters, floor, total_floors,
                    project, type, price, price_per_m2, created_at):

    # Create the SQL insert query
    insert_query = (f"INSERT INTO kengarags_prices(address,rooms,square_meters,floor_,"
                    f"total_floors,project,type_,price,price_per_m2,created_at)"
                    f" VALUES ('{address}', {rooms}, {square_meters}, {floor},"
                    f" {total_floors}, '{project}', '{type}', {price}, {price_per_m2},"
                    f"'{created_at}' )")
    try:
        # Execute the insert query
        cur.execute(insert_query)
        # Commit the transaction
        conn.commit()
    except psycopg2.Error as e:
        # Print the error and rollback the transaction in case of an error
        print(f"Error: {e}")
        conn.rollback()

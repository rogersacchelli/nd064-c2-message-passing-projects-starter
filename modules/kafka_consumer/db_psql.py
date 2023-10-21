import psycopg2
from sqlalchemy.sql import text
from typing import Dict, List
import os, logging, sys

DB_USERNAME = os.environ["DB_USERNAME"] if "DB_USERNAME" in os.environ else "ct_admin"
DB_PASSWORD = os.environ["DB_PASSWORD"] if "DB_PASSWORD" in os.environ else "wowimsosecure"
DB_PORT = os.environ["DB_PORT"] if "DB_PORT" in os.environ else 30613
DB_HOST = os.environ["DB_HOST"] if "DB_HOST" in os.environ else "localhost"
DB_NAME = os.environ["DB_NAME"] if "DB_NAME" in os.environ else "geoconnections"

logger = logging.getLogger('')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(levelname)s:%(filename)s:%(asctime)s %(message)s', datefmt='%d/%m/%Y, %H:%M:%S,')

stderr_handler = logging.StreamHandler(sys.stderr)

stderr_handler.setFormatter(formatter)
logger.addHandler(stderr_handler)

# Database connection parameters
db_params = {
    "host": DB_HOST,
    "port": DB_PORT,
    "database": DB_NAME,
    "user": DB_USERNAME,
    "password": DB_PASSWORD
}

def add_location(location_data) -> Dict:
    # Establish a connection to the database
    try:
        conn = psycopg2.connect(**db_params)
        # Create a cursor object
        cursor = conn.cursor()

        insert_query = """ insert into public.location (id, person_id, coordinate, creation_time) VALUES \
            (%(name)s, %(person_id)s, %(coordinate)s, %(creation_time)s);"""

       # Execute the insertion query
        cursor.execute(insert_query, location_data)

        # Commit the transaction
        conn.commit()

        # Close the cursor and the connection
        cursor.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)



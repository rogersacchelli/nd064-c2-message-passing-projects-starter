import psycopg2
from sqlalchemy.sql import text
from typing import Dict, List
import os, logging

DB_USERNAME = os.environ["DB_USERNAME"] if "DB_USERNAME" in os.environ else "ct_admin"
DB_PASSWORD = os.environ["DB_PASSWORD"] if "DB_PASSWORD" in os.environ else "wowimsosecure"
DB_PORT = os.environ["DB_PORT"] if "DB_PORT" in os.environ else 30613
DB_HOST = os.environ["DB_HOST"] if "DB_HOST" in os.environ else "postgres"
DB_NAME = os.environ["DB_NAME"] if "DB_NAME" in os.environ else "geoconnections"

# Database connection parameters
db_params = {
    "host": "localhost",
    "port": DB_PORT,
    "database": DB_NAME,
    "user": DB_USERNAME,
    "password": DB_PASSWORD
}

def get_close_connections(person_id, start_date, end_date, distance):
    # Establish a connection to the database
    try:
        conn = psycopg2.connect(**db_params)
        # Create a cursor object
        cursor = conn.cursor()
        # Get Locations for user first
        location_query = """ SELECT  ST_X(coordinate), ST_Y(coordinate) FROM location \
            WHERE   person_id = '{person_id}'\
            AND TO_DATE('{start_date}', 'YYYY-MM-DD') <= creation_time \
            AND     TO_DATE('{end_date}', 'YYYY-MM-DD') > creation_time;""".format(person_id=person_id, start_date=start_date, end_date=end_date)

        cursor.execute(location_query)

        # Fetch and print the results
        locations = cursor.fetchall()
        location_list = []
        for loc in locations:
            print(str(loc))
            location_list.append(loc)
        
        # Clean repeated results
        location_list = list(set(location_list))

        connections = []

        for coord_x, coord_y in location_list:

            query = """ SELECT  person_id, id, ST_X(coordinate), ST_Y(coordinate), creation_time FROM location \
                WHERE   TO_DATE('{start_date}', 'YYYY-MM-DD') <= creation_time \
                AND     TO_DATE('{end_date}', 'YYYY-MM-DD') > creation_time \
                AND     person_id != '{person_id}' \
                AND     ST_DWithin(coordinate::geography,ST_SetSRID(ST_MakePoint({coord_x}, {coord_y}),4326)::geography, '{distance}');""".format(\
                    start_date=start_date, end_date=end_date,person_id=person_id, coord_x=coord_x, coord_y=coord_y, distance=distance)
        
            print(query)

            # Execute a simple query
            cursor.execute(query)

            # Fetch and print the results
            rows = cursor.fetchall()

            for row in rows:
                print(row)
                connections.append(row)

        connections = list(set(connections))
        # Close the cursor and the connection
        cursor.close()
        conn.close()

        return connections

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error:", error)


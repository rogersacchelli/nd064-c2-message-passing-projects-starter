from kafka import KafkaConsumer
from db_psql import add_location
import logging
import sys
from geoalchemy2.functions import ST_Point


logger = logging.getLogger('')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(filename)s:%(asctime)s %(message)s', datefmt='%d/%m/%Y, %H:%M:%S,')

stdout_handler = logging.StreamHandler(sys.stdout)

stdout_handler.setFormatter(formatter)
logger.addHandler(stdout_handler)


def main():

    kafka_consumer = KafkaConsumer('location', bootstrap_servers=['kafka:9094'], api_version=(4,10,1))

    for msg in kafka_consumer:
        #logging.debug("%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition,
        #                                  msg.offset, msg.key,
        #                                  msg.value))

        # Proccess Messages
        if 'location' in msg:
            location_id = msg['location_id']
            logging.info("Received ID %d", location_id)

            coord = ST_Point(msg["longitude"], msg["latitude"])

            data_insert = {
                "id": msg['id'],
                "person_id": msg['person_id'],
                "coordinate": coord,
                "creation_time":msg['creation_time'] 
            }
            # Post message to DB
            add_location(data_insert)


if __name__ == '__main__':
    main()


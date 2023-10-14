from kafka import KafkaConsumer
import logging
import sys



logger = logging.getLogger('')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(filename)s:%(asctime)s %(message)s', datefmt='%d/%m/%Y, %H:%M:%S,')

stdout_handler = logging.StreamHandler(sys.stdout)

stdout_handler.setFormatter(formatter)
logger.addHandler(stdout_handler)


def main():

    kafka_consumer = KafkaConsumer('Location', bootstrap_servers=['10.43.197.140:9092'], api_version=(4,10,1))

    for msg in kafka_consumer:
        #logging.debug("%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition,
        #                                  msg.offset, msg.key,
        #                                  msg.value))

        # Proccess Messages
        if 'Location' in msg and 'data' in msg:
            location_id = msg['location_id']
            logging.info("Received ID %d", location_id)



if __name__ == '__main__':
    main()


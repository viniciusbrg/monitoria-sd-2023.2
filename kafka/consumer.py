from confluent_kafka import Consumer, KafkaException
import sys
import getopt
import json
import logging
from pprint import pformat



if __name__ == '__main__':
    argv = sys.argv[1:]

    broker = "localhost:9094"
    group = argv[0]
    topics = argv[1:]
    # Consumer configuration
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    conf = {'bootstrap.servers': broker, 'group.id': group, 'session.timeout.ms': 6000,
            'auto.offset.reset': 'earliest', 'enable.auto.offset.store': False}

    # Create logger for consumer (logs will be emitted when poll() is called)
    # logger = logging.getLogger('consumer')
    # logger.setLevel(logging.DEBUG)
    # handler = logging.StreamHandler()
    # handler.setFormatter(logging.Formatter('%(asctime)-15s %(levelname)-8s %(message)s'))
    # logger.addHandler(handler)

    # Create Consumer instance
    # Hint: try debug='fetch' to generate some log messages
    c = Consumer(conf)

    def print_assignment(consumer, partitions):
        print('Assignment:', partitions)

    # Subscribe to topics
    c.subscribe(topics, on_assign=print_assignment)

    # Read messages from Kafka, print to stdout
    try:
        while True:
            msg = c.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())
            else:
                # Proper message
                sys.stderr.write('%% %s [%d] at offset %d with key %s:\n' %
                                 (msg.topic(), msg.partition(), msg.offset(),
                                  str(msg.key())))
                print(msg.value())
                # Store the offset associated with msg to a local cache.
                # Stored offsets are committed to Kafka by a background thread every 'auto.commit.interval.ms'.
                # Explicitly storing offsets after processing gives at-least once semantics.
                c.store_offsets(msg)

    except KeyboardInterrupt:
        sys.stderr.write('%% Aborted by user\n')

    finally:
        # Close down consumer to commit final offsets.
        c.close()
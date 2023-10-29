from confluent_kafka import Producer
import sys

if len(sys.argv) != 2:
    sys.stderr.write('Usage: %s <topic>\n' % sys.argv[0])
    sys.exit(1)

broker = "localhost:9094"
topic = sys.argv[1]

# Producer configuration
# See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
# Create Producer instance
p = Producer({'bootstrap.servers': broker})

def delivery_callback(err, msg):
    if err:
        sys.stderr.write('%% Message failed delivery: %s\n' % err)
    else:
        sys.stderr.write('%% Message delivered to %s [%d] @ %d\n' %
                         (msg.topic(), msg.partition(), msg.offset()))

# Read lines from stdin, produce each line to Kafka
for line in sys.stdin:
    try:
        # Produce line (without newline)
        p.produce(topic, line.rstrip(), callback=delivery_callback)

    except BufferError:
        sys.stderr.write('%% Local producer queue is full (%d messages awaiting delivery): try again\n' %
                         len(p))

    # Serve delivery callback queue.
    # NOTE: Since produce() is an asynchronous API this poll() call
    #       will most likely not serve the delivery callback for the
    #       last produce()d message.
    p.poll(0)

# Wait until all messages have been delivered
sys.stderr.write('%% Waiting for %d deliveries\n' % len(p))
p.flush()
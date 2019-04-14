import os
import logging
from flask import Flask, render_template

server_dir = os.path.abspath(os.path.dirname(__file__))
client_dir = os.path.join(server_dir, '../client')
build_dir = os.path.join(client_dir, 'build')
static_dir = os.path.join(build_dir, 'static')

app = Flask(__name__, template_folder=build_dir, static_folder=static_dir)
app.logger.setLevel(logging.INFO)

@app.route('/')
def hello_world():
    return render_template('index.html')

from google.cloud import pubsub_v1
import time
@app.route('/api/task')
def task():
    app.logger.info("Start task -------------")

    project_id = "emulator"
    topic_name = "test_topic"
    num_messages = 5
    subscription_name = "sub1"

    # Instantiates a publisher and subscriber client
    publisher = pubsub_v1.PublisherClient()
    subscriber = pubsub_v1.SubscriberClient()

    # The `topic_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/topics/{topic_name}`
    topic_path = subscriber.topic_path(project_id, topic_name)

    # The `subscription_path` method creates a fully qualified identifier
    # in the form `projects/{project_id}/subscriptions/{subscription_name}`
    subscription_path = subscriber.subscription_path(
        project_id, subscription_name)

    # Create the topic.
    topic = publisher.create_topic(topic_path)
    app.logger.info('\nTopic created: {}'.format(topic.name))

    # Create a subscription.
    subscription = subscriber.create_subscription(
        subscription_path, topic_path)
    app.logger.info('\nSubscription created: {}\n'.format(subscription.name))

    publish_begin = time.time()

    # Publish messages.
    for n in range(num_messages):
        data = u'Message number {}'.format(n)
        # Data must be a bytestring
        data = data.encode('utf-8')
        # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, data=data)
        app.logger.info('Published {} of message ID {}.'.format(data, future.result()))

    publish_time = time.time() - publish_begin

    messages = set()

    def callback(message):
        app.logger.info('Received message: {}'.format(message))
        # Unacknowledged messages will be sent again.
        message.ack()
        messages.add(message)

    subscribe_begin = time.time()

    # Receive messages. The subscriber is nonblocking.
    subscriber.subscribe(subscription_path, callback=callback)

    app.logger.info('\nListening for messages on {}...\n'.format(subscription_path))

    while True:
        if len(messages) == num_messages:
            subscribe_time = time.time() - subscribe_begin
            app.logger.info("\nReceived all messages.")
            app.logger.info("Publish time lapsed: {:.2f}s.".format(publish_time))
            app.logger.info("Subscribe time lapsed: {:.2f}s.".format(subscribe_time))
            break
        else:
            # Sleeps the thread at 50Hz to save on resources.
            time.sleep(1. / 50)

    return 'task'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
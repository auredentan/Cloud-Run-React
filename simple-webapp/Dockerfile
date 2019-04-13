# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.7

# Copy local code to the container image.
WORKDIR /app
COPY server/requirements.txt server/requirements.txt

# Install production dependencies.
RUN pip install -r server/requirements.txt

COPY server server

COPY client/build client/build
# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.

CMD cd server && exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
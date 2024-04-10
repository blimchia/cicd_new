FROM python:3.11

# Allow statements and log messages to immediately appear in the Cloud Run logs
ENV PYTHONUNBUFFERED True

COPY requirements.txt ./

RUN pip install -r requirements.txt

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Run the web service on container startup and use gunicorn webserver with one worker process and 5 threads.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 5 --timeout 0 main:app

FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
COPY requirements.txt /src/
RUN pip install -r requirements.txt
COPY . /src/
CMD uvicorn ip_locations.asgi:application --host 0.0.0.0 --port $PORT

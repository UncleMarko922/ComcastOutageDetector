from python:3.7.2-alpine3.8

ADD . /app/
WORKDIR /app/
RUN pip install .
RUN apk add --no-cache build-base
CMD ["python", "comcast_outage_detector/check_for_outages.py"]
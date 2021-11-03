#Base image
FROM python:3.7.2-alpine
RUN apk add --update --no-cache libxslt-dev libxml2-dev gcc g++
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY main/scraper.py .
# Runs the file, container lives until script finishes running
CMD [ "python", "./scraper.py" ]

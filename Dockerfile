
FROM python:3.7.4

RUN pip install Flask

EXPOSE 5000
WORKDIR /app

COPY app /app
CMD [ "python", "/app/app.py" ]


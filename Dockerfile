FROM python:3.7

WORKDIR /app

COPY /flask_app /app
COPY /models/vectorizer.pkl /app/models/vectorizer.pkl

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
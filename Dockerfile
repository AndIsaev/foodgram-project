FROM python:3.8.5
WORKDIR /code
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000


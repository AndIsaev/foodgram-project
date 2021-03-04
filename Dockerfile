FROM python:3.8.5
WORKDIR /code
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
<<<<<<< HEAD
CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000
=======
CMD gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000
>>>>>>> e66db7119661b511de037d3199581937775f0014

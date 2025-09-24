FROM python:3.12-slim

WORKDIR /app

# systémové knižnice pre psycopg2 a Pillow (ak budeš neskôr riešiť obrázky)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# kopírujeme až pri buildu – v runtime mountujeme volume
COPY . /app

EXPOSE 8000
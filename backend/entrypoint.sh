#!/usr/bin/env bash
set -e

# počkaj na DB
python - <<'PY'
import os, time, psycopg2
host=os.getenv("DB_HOST","db"); port=int(os.getenv("DB_PORT","5432"))
user=os.getenv("DB_USER","forklit"); pwd=os.getenv("DB_PASSWORD","forklit")
name=os.getenv("DB_NAME","forklit")
for i in range(30):
    try:
        psycopg2.connect(host=host, port=port, user=user, password=pwd, dbname=name).close()
        break
    except Exception as e:
        time.sleep(1)
else:
    raise SystemExit("DB not ready")
PY

python manage.py migrate
python manage.py collectstatic --noinput > /dev/null 2>&1 || true

# dev: autoreload + prístup zvonku
exec python manage.py runserver 0.0.0.0:8000
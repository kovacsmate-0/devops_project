FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["gunicorn", "wsgi_server:app", "-b", "0.0.0.0:8000"]
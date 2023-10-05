FROM python:3.9
FROM nginx

WORKDIR /app

copy requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

COPY app.py .


RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/

EXPOSE 80

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ['gunicorn', 'app:app', '-b', '0.0.0.0:5000']
CMD ['nginx', '-g', 'daemon off;']

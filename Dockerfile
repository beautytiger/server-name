FROM quay.io/bitnami/python:3.6.13-prod

WORKDIR /app
ADD requirements.txt /app/requirements.txt
ADD app.py /app/app.py
RUN pip3 install -r requirements.txt && chmod a+x /app/app.py

EXPOSE 8080

CMD ./app.py

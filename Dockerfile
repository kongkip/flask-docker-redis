FROM python:3.8-slim

RUN mkdir /app
COPY . /app 
WORKDIR /app

RUN pip install -r requirements.txt 
EXPOSE 5000

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]
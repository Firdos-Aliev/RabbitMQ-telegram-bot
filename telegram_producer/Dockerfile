FROM python:3.10.12

ADD producer.py telegram_bot.py requirements.txt /app/

RUN pip install -r /app/requirements.txt

ENV AMQP_USER guest
ENV AMQP_PASSWORD guest
ENV AMQP_ADDRESS 0.0.0.0
ENV AMQP_VHOST /
ENV AMQP_PORT 5672
ENV EXTERNAL_API_URL https://google.com/
ENV BOT_TOKEN 6836199799:AAFeOOGUr8nsTZnbzTMexBiWCkUwbnIbQS4

EXPOSE 8081

CMD ["python", "/app/telegram_bot.py"]

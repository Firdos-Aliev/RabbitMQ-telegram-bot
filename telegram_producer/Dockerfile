FROM python:3.10.12

ADD producer.py telegram_bot.py requirements.txt /app/

RUN pip install -r /app/requirements.txt

ENV AMQP_USER ${AMQP_USER}
ENV AMQP_PASSWORD ${AMQP_PASSWORD}
ENV AMQP_ADDRESS ${AMQP_ADDRESS}
ENV AMQP_VHOST ${AMQP_VHOST}
ENV AMQP_PORT ${AMQP_PORT}
ENV EXTERNAL_API_URL ${EXTERNAL_API_URL}
ENV BOT_TOKEN ${BOT_TOKEN}

EXPOSE 8081

CMD ["python", "/app/telegram_bot.py"]

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

from producer import MessageQueue

import json
import os

from dotenv import load_dotenv

load_dotenv()


class TelegramRabbitMQBot():

    def __init__(self):
        # Parameters
        self.BOT_TOKEN = os.environ.get("BOT_TOKEN")
        self.EXTERNAL_API_URL = os.environ.get("EXTERNAL_API_URL", "https://google.com/")
        self.LAST_MESSAGE = ""

        # messege queue create
        self.message_queue = MessageQueue(
            host=os.environ.get("AMQP_ADDRESS", "localhost"),
            port=os.environ.get("AMQP_PORT", 5672),
            virtual_host=os.environ.get("AMQP_VHOST", "/"),
            user=os.environ.get("AMQP_USER", "guest"),
            password=os.environ.get("AMQP_PASSWORD", "guest")
        )

        # init application
        app = Application.builder().token(self.BOT_TOKEN).build()

        # commands
        app.add_handler(CommandHandler('start', self.start_command))
        app.add_handler(CommandHandler('print', self.print_command))
        app.add_handler(CommandHandler('send', self.send_command))

        # messages
        app.add_handler(MessageHandler(filters.TEXT, self.message_handler))

        # start polling
        app.run_polling()


    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("Hello telegram world")
        print("Command start")


    async def print_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("print command")
        await self.message_queue.publish_message(json.dumps({"command": "print", "last_message": self.LAST_MESSAGE}))
        print("Command print")


    async def send_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("send command")
        await self.message_queue.publish_message(json.dumps({"command": "send", "last_message": self.LAST_MESSAGE, "url": self.EXTERNAL_API_URL}))
        print("Command send")


    async def message_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        # handler to remember last message
        self.LAST_MESSAGE = update.message.text
        print(f"Last message was: {self.LAST_MESSAGE}")


if __name__ == "__main__":
    print("Start")
    TelegramRabbitMQBot()
    
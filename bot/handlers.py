from django.conf import settings

import telebot


bot = telebot.TeleBot(settings.TELEGRAM_TOKEN)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

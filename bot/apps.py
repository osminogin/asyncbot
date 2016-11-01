from django.apps import AppConfig


class BotAppConfig(AppConfig):
    name = 'bot'
    verbose_name = "Bot Application"

    def ready(self):
        from .handlers import bot
        bot.polling()


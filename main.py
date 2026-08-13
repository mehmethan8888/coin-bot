import time
import telebot

print("Bot is starting...")

bot = telebot.TeleBot("8790856684:AAHjjEb0nqHPpbNMONbyH3g4GVUUu_B0m5E")

if __name__ == "__main__":
    print("Bot çalışıyor")

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Bot çalışıyor! Hazırım.")

    bot.infinity_polling()

import telebot
import datetime
bot = telebot.TeleBot("7308514832:AAGPsw3miAP7FqIk1wFk0lGItjysMBdFtus")

target_date = datetime.datetime(2025, 6, 28)

def calculate_time_remaining():
    current_date = datetime.datetime.now()
    time_remaining = target_date - current_date
    days_remaining = time_remaining.days
    if days_remaining > 0:
        return f"باقي على التاريخ المحدد: {days_remaining} يوم."
    else:
        return "لقد انتهى العد التنازلي."

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحبًا! أرسل /countdown لحساب الأيام المتبقية حتى التاريخ المحدد.")

@bot.message_handler(commands=['countdown'])
def send_countdown(message):
    countdown_message = calculate_time_remaining()
    bot.reply_to(message, countdown_message)

if __name__ == "__main__":
    print("Bot is running...")
    bot.polling(none_stop=True)

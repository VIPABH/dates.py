import telebot
import datetime
import time

bot = telebot.TeleBot("7308514832:AAGvo7qBVMG4paaulYXg4-MPQESeqAReJhs")

target_date = datetime.datetime(2024, 6, 28)  

def calculate_time_remaining():
    while True:
        current_date = datetime.datetime.now()
        time_remaining = target_date - current_date
        days_remaining = time_remaining.days

        if days_remaining > 0:
            message = f"باقي على التاريخ المحدد: {days_remaining} يوم."
            print(message)
        else:
            print("لقد انتهى العد التنازلي.")

        time.sleep(3600) 

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"حدث خطأ: {e}")

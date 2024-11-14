import telebot
import datetime
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot("7308514832:AAGPsw3miAP7FqIk1wFk0lGItjysMBdFtus")

button1 = datetime.datetime(2025, 1, 1)  # شهر رجب
button2 = datetime.datetime(2025, 1, 31)  # شهر شعبان
button3 = datetime.datetime(2025, 3, 1)  # شهر رمضان
button4 = datetime.datetime(2025, 6, 27)  # شهر محرم

def calculate_time_remaining(target_date):
    current_date = datetime.datetime.now()
    time_remaining = target_date - current_date
    days_remaining = time_remaining.days
    if days_remaining > 0:
        return f"{days_remaining}"
    else:
        return "لقد انتهى العد التنازلي."

@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username if message.from_user.username else "لا يوجد اسم مستخدم"

    markup = InlineKeyboardMarkup()

    button1_markup = InlineKeyboardButton("شهر رجب", callback_data="رجب")
    button2_markup = InlineKeyboardButton("شهر شعبان", callback_data="شعبان")
    button3_markup = InlineKeyboardButton("شهر رمضان", callback_data="رمضان")
    button4_markup = InlineKeyboardButton("شهر محرم", callback_data="محرم")
    button5_markup = InlineKeyboardButton("المطور", callback_data="المطور")

    markup.add(button1_markup, button2_markup, button3_markup, button4_markup, button5_markup)
    
    bot.send_photo(
        message.chat.id,
        "https://t.me/iamMUAOL/9",
        caption=f" اهلا [{message.from_user.first_name}](https://t.me/{username}) حياك الله! اضغط على الزر المناسب❤.",
        parse_mode="Markdown",
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == "محرم")
def handle_moharram_callback(call):
    countdown_message = calculate_time_remaining(button4)
    username = call.from_user.username if call.from_user.username else "لا يوجد اسم مستخدم"
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        f"عزيزي [{call.from_user.first_name}](https://t.me/{username}) باقي {countdown_message} يوم لشهر محرم",
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda call: call.data == "رجب")
def handle_rabi_callback(call):
    countdown_message = calculate_time_remaining(button1)
    username = call.from_user.username if call.from_user.username else "لا يوجد اسم مستخدم"
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        f"عزيزي [{call.from_user.first_name}](https://t.me/{username}) باقي {countdown_message} يوم لشهر رجب",
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda call: call.data == "شعبان")
def handle_shaban_callback(call):
    countdown_message = calculate_time_remaining(button2)
    username = call.from_user.username if call.from_user.username else "لا يوجد اسم مستخدم"
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        f"عزيزي [{call.from_user.first_name}](https://t.me/{username}) باقي {countdown_message} يوم لشهر شعبان",
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda call: call.data == "رمضان")
def handle_ramadan_callback(call):
    countdown_message = calculate_time_remaining(button3)
    username = call.from_user.username if call.from_user.username else "لا يوجد اسم مستخدم"
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        f"عزيزي [{call.from_user.first_name}](https://t.me/{username}) باقي {countdown_message} يوم لشهر رمضان",
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda call: call.data == "المطور")
def handle_developer_callback(call):
    username = call.from_user.username if call.from_user.username else "لا يوجد اسم مستخدم"
    bot.answer_callback_query(call.id)
    bot.send_photo(
        call.message.chat.id,
       "https://t.me/LIHHIHL/108",
        "مطور هذا البوت [VIPABH](https://t.me/@k_4x1)",
        parse_mode="Markdown"
    )

if __name__ == "__main__":
    print("Bot is running...")
    bot.polling(none_stop=True)

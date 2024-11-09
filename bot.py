import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# قم بإنشاء بوت جديد باستخدام التوكن الخاص بك
bot = telebot.TeleBot("7273443857:AAFVj4Miag_IBayHn0uzYNlQz2iGD8goEz8")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    # إنشاء زر انلاين لإرسال الفيديو
    button = InlineKeyboardButton("اضغط هنا لإرسال فيديو", callback_data="send_video")
    markup.add(button)
    bot.send_message(message.chat.id, "مرحبًا بك! اضغط على الزر أدناه لإرسال فيديو:", reply_markup=markup)

# تعريف معالجة ردود الأزرار الانلاين
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "send_video":
        # رابط الفيديو الذي سيتم إرساله
        video_url = "https://t.me/VIPABH/996"
        bot.send_video(call.message.chat.id, video_url)

# بدء البوت
bot.polling()

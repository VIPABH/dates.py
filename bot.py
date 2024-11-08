from telebot import TeleBot, types

bot = telebot.TeleBot("8155824086:AAEchPPJYWsBG1yESto-dauVkuWklAG4OGk")

keybord = types.InlineKeyboardMarkup()

keybord.add.InlineKeyboardButton("ابن هاشم", callback_data=1)

keybord.add.InlineKeyboardButton("لبن", callback_data=2)

@bot.message_handler(command=[start])

def send_message(message):

bot.send_message(chat_id=message.chat.id, text="اختر شخصية", reply_markup=keyboard)

bot.polling()

import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = os.environ.get('BOT_TOKEN')

if not TOKEN:
    print("ПОМИЛКА: Змінну BOT_TOKEN не знайдено!")
    exit(1)

bot = telebot.TeleBot(TOKEN)

# Оновлене посилання на ваш сайт
WEB_APP_URL = "https://velociton-official.github.io/vton-site/"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    
    markup = InlineKeyboardMarkup()
    
    btn_app = InlineKeyboardButton(
        text="🚀 Open Mining App", 
        web_app=WebAppInfo(url=WEB_APP_URL)
    )
    
    btn_channel = InlineKeyboardButton(
        text="📢 Official Channel", 
        url="https://t.me/telegram"
    )
    
    markup.add(btn_app)
    markup.add(btn_channel)
    
    text = (
        f"Welcome, **{user_name}**! 👋\n\n"
        f"⚡ **Velociton ($VTON)** — High-Velocity Mining & Utility Jetton on TON Blockchain.\n\n"
        f"Start mining **$pVTON** points in real-time right now!"
    )
    
    bot.send_message(
        message.chat.id, 
        text, 
        parse_mode="Markdown", 
        reply_markup=markup
    )

if __name__ == "__main__":
    print("🤖 Bot is successfully running 24/7...")
    bot.infinity_polling(skip_pending=True)

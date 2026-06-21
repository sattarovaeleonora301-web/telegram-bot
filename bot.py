import telebot
from groq import Groq

TELEGRAM_TOKEN = "8825856070:AAGYVDIjlkcN3m1OPP9nUwXRfiInZC4_knM"
GROQ_API_KEY = "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"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = Groq(api_key=GROQ_API_KEY)

@bot.message_handler(func=lambda m: True)
def handle(message):
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": message.text}],
            llama-3.1-70b-versatile 
        )
        bot.reply_to(message, response.choices[0].message.content)
    except Exception as e:
        bot.reply_to(message, f"Xato: {str(e)}")

bot.polling() 

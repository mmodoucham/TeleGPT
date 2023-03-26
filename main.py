import os
import requests
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai
from keys import openai_key, telegram_key

# Set up the OpenAI API credentials
openai.api_key = openai_key

# Set up the Telegram API credentials
bot = telegram.Bot(token=telegram_key)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! I'm a bot that can generate images and text. Type /image to generate an image, or /ask to generate text.")

def reply_to_message(update, context):
    message = update.message.text.split("/ask ", 1)[1]
    print(message)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    print(response.choices[0].text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

def generate_image(update, context):
    message = update.message.text
    print(message)
    response = requests.post(
        "https://api.openai.com/v1/images/generations",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {openai.api_key}",
        },
        json={
            "model": "image-alpha-001",
            "prompt": message,
            "num_images": 1,
            "size": "512x512",
            "response_format": "url",
        },
    )
    image_url = response.json()["data"][0]["url"]
    print(image_url)
    context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url)

def main():
    updater = Updater(bot.token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("image", generate_image))
    dp.add_handler(CommandHandler("ask", reply_to_message))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

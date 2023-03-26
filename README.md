# Telegram Bot using OpenAI's text-davinci-003 and DALL-E

This Telegram bot uses OpenAI's text-davinci-003 to generate answers and DALL-E to generate images. Users can interact with the bot using the `/ask` command to generate answers and the `/image` command to generate images.

## Getting Started

To get started with this bot, you will need to have a Telegram account and a token for your bot. You can create a new bot and obtain a token by following the instructions [here](https://core.telegram.org/bots#3-how-do-i-create-a-bot).

## Installation

To install the required packages, you can use pip:

```
pip install -r requirements.txt
```

## Usage

To use the bot, you will need to provide your bot token and OpenAI API key in a `keys.py` file:

```
telegram_key=your_bot_token_here
openai_key=your_openai_api_key_here
```

You can then start the bot by running:

```
python main.py
```

Once the bot is running, users can interact with it by sending messages in the Telegram chat. To generate an answer, they can use the `/ask` command followed by their question. For example:

```
/ask who is elon musk
```

The bot will then generate a response using OpenAI's text-davinci-003 model.

To generate an image, users can use the `/image` command followed by their prompt. For example:

```
/image a cute little cat
```

The bot will then generate an image using DALL-E.

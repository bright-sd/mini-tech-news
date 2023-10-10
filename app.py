from flask import Flask, render_template, request

import requests
import json

from news import get_news_articles
import emoji

import config

from loguru import logger

logger.add("logs/bot.log",
           rotation="00:00",
           format="{time:YYYY-MM-DD at HH:mm:ss} {level} {message}",
           level="INFO")

app = Flask(__name__)

app.secret_key = config.FLASK_SECRET_KEY


@app.route("/", methods=['POST'])
def bot():
    request_json = request.json
    logger.info(f"Bot received update\n{json.dumps(request_json, indent=4)}")

    message = request.json.get('message')

    if message.get('text') == "/start":
        message_url = config.BOT_URL + 'sendMessage'

        chat = message.get('chat')
        if chat is not None:
            chat_id = chat.get('id')

            inline_keyboard_markup = [[{
                "text": f"Read Tech News {emoji.NEWSPAPER}",
                "web_app": {
                    "url": config.WEB_APP_URL
                }
            }]]

            reply_text = f"<b>Hello there! Welcome to Mini Tech News App</b> {emoji.ROLLED_UP_NEWSPAPER}\n\n"
            reply_text += "<i>Let's catch up on the latest tech news. Simply tap the button below to open the app!</i>"

            reply_data = {
                "chat_id": chat_id,
                "text": reply_text,
                "parse_mode": "HTML",
                "reply_markup": {
                    'inline_keyboard': inline_keyboard_markup
                }
            }

            response = requests.post(message_url, json=reply_data)
            response_json = response.json()
            logger.info(f"Bot update send message response:\n {json.dumps(response_json, indent=4)}")

    return "Success", 200


@app.route("/webapp", methods=['GET'])
def webapp():
    news_articles = get_news_articles()

    if news_articles is not None:
        return render_template(
            'index.html',
            news_articles=news_articles,
            emoji=emoji
        )
    else:
        error = "An error occured while fetching latest tech news"
        return render_template(
            'index.html',
            news_articles=news_articles,
            emoji=emoji,
            error=error
        )


@app.route("/webapp-close", methods=['POST'])
def webapp_close():
    user_id = request.form['user_id']
    logger.info(f"App closed by user id: {user_id}")
    message_url = config.BOT_URL + 'sendMessage'

    message_text = f"<b>All caught up on the latest tech news</b> {emoji.CHECK_MARK}\n\n"
    message_text += f"<i>Feel free to return anytime to get more updates. Have a great day!</i> {emoji.WAVING_HAND}"

    reply_data = {
        "chat_id": user_id,
        "text": message_text,
        "parse_mode": "HTML"
    }

    response = requests.post(message_url, json=reply_data)
    response_json = response.json()
    logger.info(f"App closed send message response:\n {json.dumps(response_json, indent=4)}")

    return "Success", 200


app.run(host="0.0.0.0", port=8080, debug=config.DEBUG)

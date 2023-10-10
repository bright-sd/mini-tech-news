# Mini Tech News

Telegram Mini App to help users catch up on the latest tech news.

## Overview

Mini Tech News is a Telegram Mini App that delivers the latest tech news directly to users. It offers a range of features to enhance the user's experience, including personalized greetings and message on closing the app.

## Features

- Accessible via bot menu and inline keyboard options.
- Delivers the latest tech news daily.
- Allows users to open news articles externally to access the source.
- Personalizes user interaction by greeting them with their first name.
- Sends a Telegram message to the user upon closing the app.
- Includes robust error handling.

## Technologies Used

- Flask
- Semantic UI
- requests (Telegram Bot API)

## Setup Guide

### Project Structure

- **Static**: Contains the CSS file for styling.
- **Templates**: Holds the Flask template file for the web app.
- **app.py**: Contains the application logic and routes for the web app.
- **config.py**: Loads environment variables required for the web app to run.
- **Utilities**: Includes various utility files, such as `emoji.py` for emoji constants and `news.py` for fetching tech news.

### News API

To fetch news articles, register and obtain an API key from [News API](https://newsapi.org/).

### Webhook

Set up a webhook to receive bot updates from Telegram. In `webhook.py`, replace the values of `bot_token` and `app_url`, then run the script. `app_url` should be the URL where bot updates will be received.

### Environment Variables

For the app to run, set the following environment variables:

- `FLASK_SECRET_KEY`: Flask secret key.
- `APP_URL`: Base URL of the app.
- `BOT_TOKEN`: Telegram bot token.
- `NEWS_API_KEY`: News API key obtained earlier.

### Deploying the App

You can deploy the app on various platforms, such as DigitalOcean Apps, Replit, Azure App Services, Google Cloud App Engine, or a virtual machine (VM). Choose the platform that suits your needs.

## License

MIT License

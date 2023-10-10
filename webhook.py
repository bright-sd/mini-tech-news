import json

import requests

bot_token = "BOT_TOKEN"
app_url = "APP_URL"
set_webhook_url = f"https://api.telegram.org/bot{bot_token}/setWebHook?url={app_url}"
verify_webhook_url = f"https://api.telegram.org/bot{bot_token}/getWebhookInfo"


set_response = requests.get(set_webhook_url)
set_response_json = set_response.json()

print(json.dumps(set_response_json))

verify_response = requests.get(verify_webhook_url)
verify_response_json = verify_response.json()

print(json.dumps(verify_response_json))

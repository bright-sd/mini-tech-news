import json

import requests

bot_token = ""
app_url = ""
set_webhook_url = f"https://api.telegram.org/bot{bot_token}/setWebHook?url={app_url}"
verify_webhook_url = f"https://api.telegram.org/bot{bot_token}/getWebhookInfo"


set_response = requests.get(set_webhook_url)
set_response_json = set_response.json()

json.dumps(set_response_json)

verify_response = requests.get(verify_webhook_url)
verify_response_json = verify_response.json()

json.dumps(verify_response_json)

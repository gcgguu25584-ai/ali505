from flask import Flask, request
import requests
import os

app = Flask(__name__)

# بياناتك من Green-API (تأكد من وضع التوكن الخاص بك)
ID_INSTANCE = '7107550486'
API_TOKEN_INSTANCE = '703e390c5874457eb88680d603170335' 
API_URL = 'https://7107.api.greenapi.com'

def send_reply(chatId, text):
    url = f"{API_URL}/waInstance{ID_INSTANCE}/sendMessage/{API_TOKEN_INSTANCE}"
    payload = {
        "chatId": chatId, 
        "message": text + "\n\n---\n⚡ *بواسطة: المتمرد اليماني 505*"
    }
    requests.post(url, json=payload)

@app.route('/')
def home():
    return "نظام المتمرد اليماني 505 يعمل!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    try:
        if data['typeWebhook'] == 'incomingMessageReceived':
            chatId = data['senderData']['chatId']
            user_msg = data['messageData']['textMessageData']['textMessage']
            
            if "تفعيل" in user_msg:
                send_reply(chatId, "✅ تم تفعيل نظام المتمرد اليماني 505 بنجاح!")
            else:
                send_reply(chatId, f"وصلت رسالتك: {user_msg}")
    except:
        pass
    return 'OK', 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

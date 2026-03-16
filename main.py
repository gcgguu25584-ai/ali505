from flask import Flask, request
import requests
import os

app = Flask(__name__)

# --- [ بروتوكول الحقوق: المتمرد اليماني 505 ] ---
DEV_INFO = {
    "name": "المتمرد اليماني 505",
    "telegram": "https://t.me/YWSF_ALTAEZI_VIP",
    "youtube": "https://www.youtube.com/@505-e6x",
    "phone": "+967733281285"
}

@app.route('/')
def status():
    # رسالة تظهر عند فتح رابط السيرفر للتأكد أنه يعمل
    return f"Status: Active | Developer: {DEV_INFO['name']} 🇾🇪"

@app.route('/webhook', methods=['POST'])
def whatsapp_logic():
    # هنا يتم استقبال الرسائل من الواتساب ومعالجتها
    data = request.get_json()
    print(f"Received Data: {data}")
    return "OK", 200

if __name__ == "__main__":
    # الحصول على المنفذ من Railway تلقائياً
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

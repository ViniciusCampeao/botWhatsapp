import time
import webbrowser
import pyautogui
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Envie mensagens no WhatsApp Web!"

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    numbers = data.get("numbers", "").split(",")
    message = data.get("message", "")

    if not numbers or not message:
        return jsonify({"error": "Por favor, preencha todos os campos!"}), 400

    for number in numbers:
        number = number.strip()
        if not number.startswith('+'):
            return jsonify({"error": f"Formato de número inválido: {number}"}), 400
        
        url = f"https://web.whatsapp.com/send?phone={number}&text={message}"
        webbrowser.open(url)
        time.sleep(20)
        pyautogui.press('enter')
        time.sleep(6)

    return jsonify({"success": "Mensagens enviadas com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)

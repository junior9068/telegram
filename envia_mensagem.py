import requests

def envia_mensagem(token, chat_id, msg):
    """Envia mensagem para uma sala específica no Telegram"""
    try:
        data = {"chat_id": chat_id, "text": msg}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        requests.post(url, data)
    except Exception as erro:
        print("Erro no sendMessage:", erro)

envia_mensagem("TOKEN", "CHAT-ID", "MENSAGEM")

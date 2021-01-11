import requests
import json
import configparser as cfg
import telegram


class BaccaratGame_bot():
    def __init__(self, config):
        self.token = self.read_token(config)
        self.base = "https://api.telegram.org/bot{}".format(self.token)
        self.bot = telegram.Bot(self.token)

    def get_updates(self, offset=None):
        url = self.base + "/getUpdates?timeout=100"
        if offset:
            url += "&offset={}".format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id):
        url = self.base + "/sendMessage?chat_id={}&text={}".format(chat_id, msg)
        if msg is not None:
            requests.get(url)
    
    def send_buttonmessage(self, msg, chat_id, reply):
        url = self.base + "/sendMessage?chat_id={}&text={}&reply_markup={}".format(chat_id, msg, reply)
        if msg is not None:
            requests.get(url)
    

    def read_token(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'token')


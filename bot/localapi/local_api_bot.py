# encoding:utf-8

import requests

from bot.bot import Bot
from bridge.reply import Reply, ReplyType




class LocalApiBot(Bot):
    def reply(self, query, context=None):
        url = "http://127.0.0.1:8000"
        post_data = {"prompt": query, "history": []}

        print(post_data)
        headers = {"content-type": "application/x-www-form-urlencoded"}
        response = requests.post(url, json=post_data, headers=headers)
        if response:
            reply = Reply(
                ReplyType.TEXT,
                response.json()["response"],
            )
            return reply



from typing import Any

import requests

from bot.tg.dc import GetUpdatesResponse, SendMessageResponse
from todolist import settings


class TgClient:
    def __init__(self, token: str = None) -> None:
        self.__token = token if token else settings.BOT_TOKEN
        self.__base_url = f"https://api.telegram.org/bot{self.__token}/"

    def get_updates(self, offset: int = 0, timeout: int = 60) -> GetUpdatesResponse:
        data = self._get('getUpdates', offset=offset, timeout=timeout)
        return GetUpdatesResponse(**data)

    def send_message(self, chat_id: int, text: int) -> SendMessageResponse:
        data = self._get('sendMessage', chat_id=chat_id, text=text)
        return SendMessageResponse(**data)

    def __get_url(self, method: str) -> str:
        return f'{self.__base_url}{method}'

    def _get(self, command: str, **params: Any) -> dict:
        url = self.__get_url(command)
        response = requests.get(url, params=params)
        if not response.ok:
            print(f'Invalid {response.status_code} an command {command}')
            return {'ok': False, 'result': []}
        return response.json()





    # def get_url(self, method: str) -> str:
    #     """ URL для запроса к Telegram боту через токен """
    #     return f"https://api.telegram.org/bot{self.token}/{method}"
    #
    # def get_updates(self, offset: int = 0, timeout: int = 60) -> GetUpdatesResponse:
    #     """ Получение ботом исходящих сообщений от пользователя """
    #     url = self.get_url("getUpdates")
    #     resp = requests.get(url, params={"offset": offset, "timeout": timeout,
    #                                      "allowed_updates": ["update_id", "message"]})
    #     return GetUpdatesResponse.Schema().load(resp.json())
    #
    # def send_message(self, chat_id: int, text: str) -> SendMessageResponse:
    #     """ Получение пользователем сообщений от бота """
    #     url = self.get_url("sendMessage")
    #     resp = requests.post(url, params={"chat_id": chat_id, "text": text})
    #     return SendMessageResponse.Schema().load(resp.json())

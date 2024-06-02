import time
from typing import Optional, Union

from pydantic import ValidationError
from requests import Session, Response
from requests.utils import default_headers, CaseInsensitiveDict

from hamster.hamster_objects import (TaskList, ClickerUserWrapper,
                                     ResponseGetMe, BoostsForBuy,
                                     BoostId, ResponseModelBuyBoost, ErrorResponse)


# code by: https://t.me/cazqev
# version: 01.06.2024


class BasicApi:
    __basic_url__ = 'https://donate.cazqev.com/'

    def __init__(self, headers: Optional[dict] = None,
                 session: Optional[Session] = None):
        self.headers = headers or default_headers()
        self.session = session or Session()
        self.__update_session_headers()

    def add_bearer(self, token: str):
        self.headers.update(
            {'Authorization': f'Bearer {token}'}
        )
        self.__update_session_headers()

    def make_request(self, path: str, method: str, **kwargs) -> Response:
        r = self.session.request(
            method=method,
            url=self.__basic_url__ + path,
            **kwargs
        )
        return r

    def __update_session_headers(self):
        self.session.headers.update(CaseInsensitiveDict(self.headers))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


class Hamster(BasicApi):
    __basic_url__ = 'https://api.hamsterkombat.io/'

    def __init__(self, *, auth_key: str):
        super().__init__()
        self.add_bearer(auth_key)


    def list_tasks(self) -> Optional[Union[dict, TaskList]]:
        response = self.make_request('clicker/list-tasks', 'POST')
        if response.ok:
            return TaskList.model_validate(response.json())
        else:
            return {
                'error': response.text,
            }

    def sync(self) -> Optional[Union[dict, ClickerUserWrapper]]:
        response = self.make_request('clicker/sync', 'POST')
        if response.ok:
            return ClickerUserWrapper.model_validate(response.json())
        else:
            return {
                'error': response.text,
            }

    def get_me(self) -> Optional[Union[dict, ResponseGetMe]]:
        response = self.make_request('auth/me-telegram', 'POST')
        if response.ok:
            return ResponseGetMe.model_validate(response.json())
        else:
            return {
                'error': response.text,
            }

    def tap(self, count: int, available_taps: Optional[int] = None) -> Optional[Union[dict, ClickerUserWrapper]]:
        if available_taps is None:
            synced = self.sync()
            if isinstance(synced, ClickerUserWrapper):
                available_taps = synced.clickerUser.availableTaps
            else:
                return synced

        if available_taps < count:
            return {
                'error': 'Для безопасности аккаунта, Вы не можете нажать больше раз чем вам доступно',
                'avaliable': available_taps,
            }

        timestamp = int(time.time())
        response = self.make_request('clicker/tap', 'POST',
                                     json={'availableTaps': available_taps,
                                           'count': count,
                                           'timestamp': timestamp})
        if response.ok:
            return ClickerUserWrapper.model_validate(response.json())
        else:
            return {
                'error': response.text,
            }

    def boosts_for_buy(self):
        response = self.make_request('clicker/boosts-for-buy', 'POST')
        if response.ok:
            return BoostsForBuy.model_validate(response.json())
        else:
            return {
                'error': response.text
            }

    def buy_boost(self, boost_id: BoostId) -> Optional[Union[dict, ResponseModelBuyBoost, ErrorResponse]]:
        timestamp = int(time.time())
        response = self.make_request('clicker/buy-boost', 'POST',
                                     json={'boostId': boost_id.value, 'timestamp': timestamp})
        if response.ok:
            return ResponseModelBuyBoost.model_validate(response.json())
        else:
            try:
                error_response = ErrorResponse.model_validate(response.json())
                return error_response
            except ValidationError:
                return {'error': response.text}

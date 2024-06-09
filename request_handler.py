import json
import os

import requests
import requests_cache
from constants import CONFIG_PATH, API_URL, CACHE_PATH


class RequestHandler:

    def __init__(self, date, base_currency):
        self.__base_currency = base_currency
        self.__config = self.__get_config(CONFIG_PATH)
        self.__api_url = self.__get_api_url(date, base_currency, self.__get_api_key())

    def __get_config(self, config_path):
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
        return config

    def __get_api_key(self):
        return self.__config["api_key"]

    def __get_api_url(self, date, base_currency, api_key):
        return API_URL.format(date=date, base_currency=base_currency, api_key=api_key)

    def fetch_base_currency_data(self):
        if not os.path.exists("cache"):
            os.makedirs("cache")
        requests_cache.install_cache(f"{CACHE_PATH}{self.__base_currency}")
        headers = {"accept": "application/json"}
        response = requests.get(self.__api_url, headers=headers)
        currencies_list = response.json()["results"]
        return currencies_list

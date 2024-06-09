import json
import os.path

from constants import CONVERSIONS_PATH
from input_handler import InputHandler
from request_handler import RequestHandler


class CurrencyConvertor:

    def __init__(self):
        self.__date = None
        self.__amount = None
        self.__base_currency = None
        self.__target_currency = None
        self.__exchange_rate = None
        self.__request_handler = None
        self.__input_handler = InputHandler()

    def __get_final_output(self):
        converted_amount = float(self.__exchange_rate) * float(self.__amount)
        rounded_converted_amount = round(converted_amount, 2)
        print(
            f"{self.__amount} {self.__base_currency} is equal to {rounded_converted_amount} {self.__target_currency}. ")
        self.__save_conversion_to_file(rounded_converted_amount)

    def __save_conversion_to_file(self, rounded_converted_amount):
        data = {
            "date": self.__date,
            "base_currency": self.__base_currency,
            "amount": self.__amount,
            "target_currency": self.__target_currency,
            "converted_amount": rounded_converted_amount,
            "exchange_rate": self.__exchange_rate
        }

        if not os.path.exists("successful_conversions"):
            os.makedirs("successful_conversions")

        file_path = f"{CONVERSIONS_PATH}{self.__base_currency}_{self.__amount}_to_{self.__target_currency}.json"

        if not os.path.exists(file_path):
            with open(file_path, 'w') as conversion_file:
                json.dump(data, conversion_file, indent=4)

    def run(self):
        self.__date = self.__input_handler.get_date_argument()
        while True:
            self.__amount = self.__input_handler.get_amount_input()
            self.__base_currency = self.__input_handler.get_currency_input()
            self.__request_handler = RequestHandler(self.__date, self.__base_currency)
            currencies_list = self.__request_handler.fetch_base_currency_data()
            self.__target_currency = self.__input_handler.get_currency_input()
            self.__exchange_rate = currencies_list[self.__target_currency]
            self.__get_final_output()

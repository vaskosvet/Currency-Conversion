import argparse
import atexit
import os.path
import re
import sys
from datetime import datetime

import requests_cache
from iso4217 import Currency

from constants import OFFSHORE_YUAN_CODE, END_COMMAND, INVALID_CURRENCY_MESSAGE, INVALID_AMOUNT_MESSAGE, \
    AMOUNT_REGEX_PATTERN, INVALID_DATE_MESSAGE, DATE_FORMAT, CACHE_PATH, CONVERSIONS_PATH


def _cleanup():
    __cleanup_cache()
    __cleanup_successful_conversions()


def __cleanup_cache():
    requests_cache.clear()
    for cache_file in os.listdir(CACHE_PATH):
        file_path = os.path.join(CACHE_PATH, cache_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)


def __cleanup_successful_conversions():
    for conversion in os.listdir(CONVERSIONS_PATH):
        file_path = os.path.join(CONVERSIONS_PATH, conversion)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)


class InputHandler:
    atexit.register(_cleanup)

    def get_date_argument(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("input_date", type=self.__validate_date)
        args = parser.parse_args()
        converted_date = datetime.strftime(args.input_date, DATE_FORMAT)
        return converted_date

    def __validate_date(self, date):
        try:
            today_date = datetime.today().date()
            converted_date = datetime.strptime(date, DATE_FORMAT)
            if converted_date.date() >= today_date:
                print(INVALID_DATE_MESSAGE)
                self.__end_application()
            else:
                return converted_date
        except ValueError:
            raise argparse.ArgumentTypeError(INVALID_DATE_MESSAGE)

    def __end_application(self):
        sys.exit(0)

    def get_amount_input(self):
        while True:
            amount = input()
            if amount.lower() == END_COMMAND:
                self.__end_application()
            if re.match(AMOUNT_REGEX_PATTERN, amount):
                return float(amount)
            else:
                print(INVALID_AMOUNT_MESSAGE)

    def __is_currency_valid(self, currency):
        try:
            if currency.upper() == OFFSHORE_YUAN_CODE:  # iso4217 library does not recognize CNH
                return True
            Currency(currency.upper())
            return True
        except ValueError:
            return False

    def __validate_currency(self, currency):
        if self.__is_currency_valid(currency):
            return True
        else:
            return False

    def get_currency_input(self):
        while True:
            currency = input()
            if currency.lower() == END_COMMAND:
                self.__end_application()
            if self.__validate_currency(currency):
                return currency.upper()
            else:
                print(INVALID_CURRENCY_MESSAGE)

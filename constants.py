API_URL = "https://api.fastforex.io/historical?date={date}&from={base_currency}&api_key={api_key}"

END_COMMAND = "end"
OFFSHORE_YUAN_CODE = "CNH"
DATE_FORMAT = "%Y-%m-%d"
AMOUNT_REGEX_PATTERN = r"^(?!0$)\d+(\.\d{1,2})?$"

INVALID_CURRENCY_MESSAGE = "Please, enter a valid currency."
INVALID_DATE_MESSAGE = "Please, enter a valid date."
INVALID_AMOUNT_MESSAGE = "Please, enter a valid amount."

CONFIG_PATH = "config.json"
CACHE_PATH = "cache/"
CONVERSIONS_PATH = "successful_conversions/"

from datetime import datetime, timezone
from json import dumps, loads
from re import sub


class Formatter:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Formatter, cls).__new__(cls)
        return cls.__instance

    def bytes_to_str(self, obj: bytes | bytearray):
        str_payload = obj.decode("utf-8")
        return loads(str_payload)

    def datetime_to_isoformat(self, date_time: datetime) -> str:
        return date_time.replace(tzinfo=timezone.utc).isoformat().replace("+00:00", "Z")

    def str_to_bytes(self, obj: dict):
        json_str = dumps(obj)
        return json_str.encode("utf-8")

    def camel_to_snake(self, key: str) -> str:
        snake_case_key = sub("(.)([A-Z][a-z]+)", r"\1_\2", key)
        return sub("([a-z0-9])([A-Z])", r"\1_\2", snake_case_key).lower()

    def snake_to_camel(self, key: str) -> str:
        words = key.split("_")
        return words[0] + "".join(letter.title() for letter in words[1:])


fmt = Formatter()

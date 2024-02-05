from functools import lru_cache
from logging import basicConfig, getLogger, INFO


class AppLogger:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(AppLogger, cls).__new__(cls)
            cls.__instance.__setup_logger()
        return cls.__instance

    def __setup_logger(self):
        basicConfig(
            format="%(levelname)s:     %(asctime)s - %(name)s - %(message)s", level=INFO, datefmt="%Y-%m-%d %H:%M:%S"
        )
        self.logger = getLogger(name="PLENO")

    def crit(self, msg: str, exc_info: bool = False):
        return self.logger.critical(msg=msg, exc_info=exc_info)

    def bug(self, msg: str, exc_info: bool = False):
        return self.logger.debug(msg=msg, exc_info=exc_info)

    def err(self, msg: str, exc_info: bool = False):
        return self.logger.error(msg=msg, exc_info=exc_info)

    def info(self, msg: str, exc_info: bool = False):
        return self.logger.info(msg=msg, exc_info=exc_info)

    def warn(self, msg: str, exc_info: bool = False):
        return self.logger.warning(msg=msg, exc_info=exc_info)


@lru_cache()
def get_logger() -> AppLogger:
    return AppLogger()


log = get_logger()

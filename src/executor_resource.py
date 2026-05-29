from src.logger import log, log_error

class ExecutorResource:

    def __init__(self, logger=None):
        self.logger = logger or log

    async def __aenter__(self):
        self.logger.info("ресурс открыт")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            log_error(f"ошибка в ресурсе: {exc_val}")
        self.logger.info("ресурс закрыт")
        return False

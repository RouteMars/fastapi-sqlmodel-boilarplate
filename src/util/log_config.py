import logging
import sys

import sqlparse
from loguru import logger


class SQLFormatter(logging.Handler):
    def emit(self, record):
        # msg = self.format(record)
        msg = record.getMessage().strip()
        if any(kw in msg.upper() for kw in ["COMMIT", "ROLLBACK", "BEGIN", "DESCRIBE", "[RAW SQL]"]):
            return
        msg = sqlparse.format(msg, reindent=True, keyword_case="upper")
        logger.debug(f"Query\n{msg}\n")


def setup_logging():
    try:
        # Default
        logger.remove()
        logger.level("DEBUG", color="<magenta>")
        logger.level("INFO", color="<green>")
        # logger.level("WARNING", color="<yellow>")
        # logger.level("ERROR", color="<red>")
        # logger.level("CRITICAL", color="<RED><bold>")
        format = "<level>{level}</level> - {message}"
        # format = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> - {message}"
        logger.add(sys.stdout, format=format, colorize=True)

        # SQL
        sqlalchemy_logger = logging.getLogger("sqlalchemy.engine")
        sqlalchemy_logger.setLevel(logging.INFO)
        sqlalchemy_logger.handlers = []
        sqlalchemy_logger.addHandler(SQLFormatter())
    except Exception as e:
        # logger.add("logs/fallback.log", level="DEBUG")
        logger.error(f"stdout 로그 설정 실패: {e}")

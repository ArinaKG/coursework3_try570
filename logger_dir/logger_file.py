import logging

logger_one = logging.getLogger("one")
logger_two = logging.getLogger("two")

file_handler_one = logging.FileHandler("log_one.txt")
file_handler_two = logging.FileHandler("log_two.txt")

logger_one.addHandler(file_handler_one)
logger_two.addHandler(file_handler_two)

logger_one.warning("Запись для логгера один")
logger_two.warning("Запись для логгера два")
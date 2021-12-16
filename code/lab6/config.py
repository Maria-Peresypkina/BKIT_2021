from enum import Enum

# Токент бота
TOKEN = "5015617089:AAHDaX6zRPxORWEcZsPgMweqHNWKke4X82g"

# Файл базы данных Vedis
db_file = "db.vdb"

# Ключ записи в БД для текущего состояния
CURRENT_STATE = "CURRENT_STATE"

# Состояния автомата
class States(Enum):
    STATE_START = "STATE_START"  # Начало нового диалога
    S_ENTER_NAME = "S_ENTER_NAME"
    S_ENTER_AGE = "S_ENTER_AGE"
    S_SEND_PIC = "S_SEND_PIC"
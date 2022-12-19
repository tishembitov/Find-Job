from config import DATABASE_URI                 # параметры подключения к БД из модуля конфигурации config.py
from .repository.connectorfactory import *       # подключаем фабрику коннекторов к БД
from .repository.sql_api import *                # подключаем API для работы с БД

"""
    В данном модуле реализуются логика обработки клиентских запросов.
    Здесь также могут применяться SQL-методы, представленные в модуле repository.sql_api
"""

# Получаем список обработанных файлов
def get_vacancy_list():
    db_connector = SQLStoreConnectorFactory().get_connector(DATABASE_URI)  # получаем объект соединения
    result = select_all_from_vacancy(db_connector)  # получаем список всех обработанных файлов
    # Завершаем работу с БД
    db_connector.close()
    return result

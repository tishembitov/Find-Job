from processor.dataprocessorfactory import *    # подключаем фабрику обработчиков данных
from repository.connectorfactory import *       # подключаем фабрику коннекторов к БД
from repository.sql_api import *                # подключаем API для работы с БД
import time

"""
    Данный модуль запускает программу
        ("точка входа" приложения)
"""
DATASOURCE1 = "user.csv"
DATASOURCE2 = "resume.csv"
DATASOURCE3 = "vacancy.csv"
DB_URL = 'sqlite:///test.db'

# В зависимости от расширения файла вызываем соответствующий фабричный метод
def init_processor(source: str) -> DataProcessor:
    proc = None
    if source.endswith('.csv'):
        proc = CsvDataProcessorFactory().get_processor(source)
    elif source.endswith('.txt'):
        proc = TxtDataProcessorFactory().get_processor(source)
    return proc

# Запуск обработки
def run_processor(proc: DataProcessor) -> DataFrame:
    proc.run()
    proc.print_result()
    return proc.result

def delete_all():
    db_connector = SQLStoreConnectorFactory().get_connector(DB_URL)  # получаем объект соединения
    delete_from_user(db_connector)
    delete_from_vacancy(db_connector)
    delete_from_resume(db_connector)
    delete_from_mydocuments(db_connector)
    delete_from_source_files(db_connector)
    delete_from_myresumes(db_connector)
    delete_from_myvacancies(db_connector)
    db_connector.close()

def insert():
    result1 = None  # результат обработки данных
    # Запуск обработчика данных
    proc1 = init_processor(DATASOURCE1)
    if proc1 is not None:
        result1 = run_processor(proc1)

    # Работа с БД
    if result1 is not None:
        db_connector = SQLStoreConnectorFactory().get_connector(DB_URL)  # получаем объект соединения
        insert_into_source_files(db_connector, DATASOURCE1)  # сохраняем в БД информацию о файле с набором данных
        print(select_all_from_source_files(db_connector))  # вывод списка всеъ обработанных файлов
        insert_rows_into_user_data(db_connector, result1.iloc[:5])  # записываем в БД 5 первых строк результата
        db_connector.close()
    result2 = None  # результат обработки данных
    # Запуск обработчика данных
    proc2 = init_processor(DATASOURCE2)
    if proc2 is not None:
        result2 = run_processor(proc2)

    # Работа с БД
    if result2 is not None:
        db_connector = SQLStoreConnectorFactory().get_connector(DB_URL)  # получаем объект соединения
        insert_into_source_files(db_connector, DATASOURCE2)  # сохраняем в БД информацию о файле с набором данных
        print(select_all_from_source_files(db_connector))  # вывод списка всеъ обработанных файлов
        insert_rows_into_resume_data(db_connector, result2.iloc[:5])  # записываем в БД 5 первых строк результата
        db_connector.close()

    result3 = None  # результат обработки данных
    # Запуск обработчика данных
    proc3 = init_processor(DATASOURCE3)
    if proc3 is not None:
        result3 = run_processor(proc3)

    # Работа с БД
    if result3 is not None:
        db_connector = SQLStoreConnectorFactory().get_connector(DB_URL)  # получаем объект соединения
        insert_into_source_files(db_connector, DATASOURCE3)  # сохраняем в БД информацию о файле с набором данных
        print(select_all_from_source_files(db_connector))  # вывод списка всеъ обработанных файлов
        insert_rows_into_vacancy_data(db_connector, result3.iloc[:5])  # записываем в БД 5 первых строк результата
        # Завершаем работу с БД
    insert_rows_into_mydocuments_data(db_connector)  # записываем в БД 5 первых строк результата
    insert_rows_into_myresumes_data(db_connector)  # записываем в БД 5 первых строк результата
    insert_rows_into_myvacancies_data(db_connector)  # записываем в БД 5 первых строк результата
    db_connector.close()

if __name__ == '__main__':
    #delete_all()
    insert()

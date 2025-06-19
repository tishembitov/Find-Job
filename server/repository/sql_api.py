from .connector import StoreConnector
from pandas import DataFrame, Series
from datetime import datetime

"""
    В данном модуле реализуется API (Application Programming Interface)
    для взаимодействия с БД с помощью объектов-коннекторов.
    
    ВАЖНО! Методы должны быть названы таким образом, чтобы по названию
    можно было понять выполняемые действия.
"""
# Вывод списка обработанных файлов с сортировкой по дате
def select_all_from_source_files(connector: StoreConnector):
    connector.start_transaction()  # начинаем выполнение запросов
    query = f'SELECT * FROM source_files ORDER BY processed'
    result = connector.execute(query).fetchall()
    connector.end_transaction()  # завершаем выполнение запросов
    return result

# Вставка в таблицу обработанных файлов
def insert_into_source_files(connector: StoreConnector, filename: str):
    now = datetime.now() # текущая дата и время
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")   # преобразуем в формат SQL
    connector.start_transaction()
    query = f'INSERT INTO source_files (filename, processed) VALUES (\'{filename}\', \'{date_time}\')'
    result = connector.execute(query)
    connector.end_transaction()
    return result

# Вставка строк из DataFrame в БД
def insert_rows_into_vacancy_data(connector: StoreConnector, dataframe: DataFrame):
    rows = dataframe.to_dict('records')
    connector.start_transaction()
    for row in rows:
        connector.execute(f'INSERT INTO vacancy (name, employer, status, shedule, experience, salary, skills, city, street, building) VALUES (\'{row["vacancy_name"]}\', \'{row["employer_name"]}\', \'{row["vacancy_type"]}\', \'{row["vacancy_schedule"]}\', \'{row["vacancy_experience"]}\', \'{row["vacancy_salary"]}\', \'{row["skill_name"]}\', \'{row["city"]}\', \'{row["street"]}\', \'{row["building"]}\')')
    connector.end_transaction()

def insert_rows_into_user_data(connector: StoreConnector, dataframe: DataFrame):
    rows = dataframe.to_dict('records')
    connector.start_transaction()
    for row in rows:
        connector.execute(f'INSERT INTO user (email, password, role) VALUES (\'{row["email"]}\', \'{row["password"]}\', \'{row["role"]}\')')
    connector.end_transaction()

def insert_rows_into_resume_data(connector: StoreConnector, dataframe: DataFrame):
    rows = dataframe.to_dict('records')
    connector.start_transaction()
    for row in rows:
        connector.execute(f'INSERT INTO resume (title, first_name, last_name, middle_name, age, gender, area, education_level, experience, salary, skills) VALUES (\'{row["title"]}\', \'{row["first_name"]}\', \'{row["last_name"]}\', \'{row["middle_name"]}\', \'{row["age"]}\', \'{row["gender"]}\', \'{row["area"]}\', \'{row["education_level"]}\', \'{row["experience"]}\',  \'{row["salary"]}\', \'{row["skills"]}\')')
    connector.end_transaction()

def insert_rows_into_mydocuments_data(connector: StoreConnector):
    connector.start_transaction()
    connector.execute(f'INSERT INTO mydocuments (user_id) VALUES (57)')
    connector.end_transaction()

def insert_rows_into_myresumes_data(connector: StoreConnector):
    connector.start_transaction()
    connector.execute(f'INSERT INTO myresumes (mydocuments_id, resume_id) VALUES (8, 57)')
    connector.end_transaction()

def insert_rows_into_myvacancies_data(connector: StoreConnector):
    connector.start_transaction()
    connector.execute(f'INSERT INTO myvacancies (mydocuments_id, vacancy_id) VALUES (8, 57)')
    connector.end_transaction()


# Удаление строк
def delete_from_source_files(connector: StoreConnector):
    connector.start_transaction()
    query = f'DELETE FROM source_files WHERE id<100'
    result = connector.execute(query)
    connector.end_transaction()
    return result

def delete_from_vacancy(connector: StoreConnector):
    connector.start_transaction()
    query = f'DELETE FROM vacancy WHERE id<100'
    result = connector.execute(query)
    connector.end_transaction()
    return result

def delete_from_user(connector: StoreConnector):
    connector.start_transaction()
    query = f'DELETE FROM user WHERE id<100'
    result = connector.execute(query)
    connector.end_transaction()
    return result

def delete_from_resume(connector: StoreConnector):
    connector.start_transaction()
    query = f'DELETE FROM resume WHERE id<100'
    result = connector.execute(query)
    connector.end_transaction()
    return result

def delete_from_mydocuments(connector: StoreConnector):
    connector.start_transaction()
    query = f'DELETE FROM mydocuments WHERE id<100'
    result = connector.execute(query)
    connector.end_transaction()
    return result

def delete_from_myresumes(connector: StoreConnector):
    connector.start_transaction()
    query = f'DELETE FROM myresumes WHERE id<100'
    result = connector.execute(query)
    connector.end_transaction()
    return result

def delete_from_myvacancies(connector: StoreConnector):
    connector.start_transaction()
    query = f'DELETE FROM myvacancies WHERE id<100'
    result = connector.execute(query)
    connector.end_transaction()
    return result

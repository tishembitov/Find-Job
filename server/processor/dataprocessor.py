from abc import ABC, abstractmethod  # подключаем инструменты для создания абстрактных классов
import pandas  # библиотека для работы с датасетами
# Библиотека для работы с HTTP-запросами. Будем использовать ее для обращения к API HH
import requests
# Пакет для удобной работы с данными в формате json
import json

"""
    В данном модуле реализуются классы обработчиков для 
    применения алгоритма обработки к различным типам файлов (csv или txt).
    ВАЖНО! Если реализация различных обработчиков занимает большое 
    количество строк, то необходимо оформлять каждый класс в отдельном файле
"""


# Родительский класс для обработчиков файлов
class DataProcessor(ABC):
    def __init__(self, datasource):
        # общие атрибуты для классов обработчиков данных
        self._datasource = datasource  # путь к источнику данных
        self._dataset = None  # входной набор данных
        self.result = None  # выходной набор данных (результат обработки)

    # Метод, инициализирующий источник данных
    # Все методы, помеченные декоратором @abstractmethod, ОБЯЗАТЕЛЬНЫ для переобределения
    @abstractmethod
    def read(self) -> bool:
        pass

    # Точка запуска методов обработки данных
    @abstractmethod
    def run(self):
        pass

    """
        Пример одного из общих методов обработки данных.
        В данном случае метод просто сортирует входной датасет по значению заданной колонки (аргумент col)
        ВАЖНО! Следует логически разделять методы обработки, например, отдельный метод для сортировки, 
        отдельный метод для удаления "пустот" в датасете и т.д. Это позволит гибко применять необходимые
        методы при переопределении метода run для того или иного типа обработчика.
        НАПРИМЕР, если ваш источник данных это не файл, а база данных, тогда метод сортировки будет не нужен,
        т.к. сортировку можно сделать при выполнении SQL-запроса типа SELECT ... ORDER BY...
    """

    def sort_data_by_col(self, df, colname, asc) -> pandas.DataFrame:
        return df.sort_values(by=[colname], ascending=asc)

    # Абстрактный метод для вывоа результата на экран
    @abstractmethod
    def print_result(self):
        pass


# Реализация класса-обработчика csv-файлов
class CsvDataProcessor(DataProcessor):
    # Переобпределяем конструктор родительского класса
    def __init__(self, datasource):
        DataProcessor.__init__(self,
                               datasource)  # инициализируем конструктор родительского класса для получения общих атрибутов
        self.separator = ';'  # дополнительный атрибут - сепаратор по умолчанию

    """
        Переопределяем метод инициализации источника данных.
        Т.к. данный класс предназначен для чтения CSV-файлов, то используем метод read_csv
        из библиотеки pandas
    """

    def read(self):
        try:
            self._dataset = pandas.read_csv(self._datasource, sep=self.separator, header='infer', names=None,
                                            encoding="utf-8")
            # Читаем имена колонок из файла данных
            col_names = self._dataset.columns
            # Если количество считанных колонок < 2 возвращаем false
            if len(col_names) < 2:
                return False
            return True
        except Exception as e:
            print(str(e))
            return False

    def run(self):
        #self.result = self.sort_data_by_col(self._dataset, "vacancy_name", True)
        self.result = self._dataset.dropna(axis = 0, how ='any')

    def print_result(self):
        print(f'Running CSV-file processor!\n', self.result)


# Реализация класса-обработчика txt-файлов
class TxtDataProcessor(DataProcessor):
    # Реализация метода для чтения TXT-файла
    def read(self):
        try:
            self._dataset = pandas.read_table(self._datasource, sep='\s+', engine='python')
            col_names = self._dataset.columns
            if len(col_names) < 2:
                return False
            return True
        except Exception as e:
            print(str(e))
            return False

    def run(self):
        #self.result = self.sort_data_by_col(self._dataset, "vacancy_name", True)
        self.result = self._dataset.dropna(axis=0, how='any')

    def print_result(self):
        print(f'Running TXT-file processor!\n', self.result)


# Реализация класса-обработчика api
class APIDataProcessor(DataProcessor):
    # Реализация метода для запроса API
    def read(self):
        try:
            params = {
                'text': 'NAME:Аналитик',  # Текст фильтра. В имени должно быть слово "Аналитик"
                'area': 1,  # Поиск ощуществляется по вакансиям города Москва
                'page': 5,  # Индекс страницы поиска на HH
                'per_page': 2  # Кол-во вакансий на 1 странице
            }

            self._datasource = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
            self._dataset = self._datasource.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
            self._datasource.close()
            return True
        except Exception as e:
            print(str(e))
            return False

    def run(self):
        # Преобразуем текст ответа запроса в справочник Python
        self.result = json.loads(self._dataset)

    def print_result(self):
        print(json.dumps(self.result, ensure_ascii=False, indent=4))
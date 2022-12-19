# -*- coding: utf-8 -*-
# Подключаем объект приложения Flask из __init__.py
from labapp import app
# Подключаем библиотеку для "рендеринга" html-шаблонов из папки templates
from flask import render_template, make_response, request, Response, jsonify, json
from . import controller    # подключаем controller.py

"""
    Модуль регистрации маршрутов для запросов к серверу, т.е.
    здесь реализуется обработка запросов при переходе пользователя на определенные адреса веб-приложения
"""


# Обработка запроса к индексной странице
@app.route('/')
@app.route('/index-2.html')
def index():
    # Пример вызова метода с выборкой данных из БД и вставка полученных данных в html-шаблон
    processed_files = controller.get_vacancy_list()
    # "рендеринг" (т.е. вставка динамически изменяемых данных) в index.html и возвращение готовой страницы
    return render_template('index-2.html', title='Find Job', processed_files=processed_files)

@app.route('/job-list-1.html')
def job_list():
    # Пример вызова метода с выборкой данных из БД и вставка полученных данных в html-шаблон
    processed_files = controller.get_vacancy_list()
    # "рендеринг" (т.е. вставка динамически изменяемых данных) в index.html и возвращение готовой страницы
    return render_template('job-list-1.html', processed_files=processed_files)

@app.route('/job-add.html')
def job_add():
    # Пример вызова метода с выборкой данных из БД и вставка полученных данных в html-шаблон
    # "рендеринг" (т.е. вставка динамически изменяемых данных) в index.html и возвращение готовой страницы
    return render_template('job-add.html')

@app.route('/job-manage.html')
def job_manage():
    # Пример вызова метода с выборкой данных из БД и вставка полученных данных в html-шаблон
    processed_files = controller.get_vacancy_list()
    # "рендеринг" (т.е. вставка динамически изменяемых данных) в index.html и возвращение готовой страницы
    return render_template('job-manage.html', processed_files=processed_files)

@app.route('/user-register.html')
def user_register():
    # Пример вызова метода с выборкой данных из БД и вставка полученных данных в html-шаблон
    # "рендеринг" (т.е. вставка динамически изменяемых данных) в index.html и возвращение готовой страницы
    return render_template('user-register.html')

@app.route('/user-login.html')
def user_login():
    # Пример вызова метода с выборкой данных из БД и вставка полученных данных в html-шаблон
    # "рендеринг" (т.е. вставка динамически изменяемых данных) в index.html и возвращение готовой страницы
    return render_template('user-login.html')

@app.route('/user-forget-pass.html')
def user_forget_pass():
    # Пример вызова метода с выборкой данных из БД и вставка полученных данных в html-шаблон
    # "рендеринг" (т.е. вставка динамически изменяемых данных) в index.html и возвращение готовой страницы
    return render_template('user-forget-pass.html')
"""
Реализация response-методов, возвращающих клиенту стандартные коды протокола HTTP
"""

# Возврат html-страницы с кодом 404 (Не найдено)
@app.route('/notfound')
def not_found_html():
    return render_template('404.html', title='404', err={ 'error': 'Not found', 'code': 404 })

# Формирование json-ответа. Если в метод передается только data (dict-объект), то по-умолчанию устанавливаем код возврата code = 200
# В Flask есть встроенный метод jsonify(dict), который также реализует данный метод (см. пример метода not_found())
def json_response(data, code=200):
    return Response(status=code, mimetype="application/json", response=json.dumps(data))

# Пример формирования json-ответа с использованием встроенного метода jsonify()
# Обработка ошибки 404 протокола HTTP (Данные/страница не найдены)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)

# Обработка ошибки 400 протокола HTTP (Неверный запрос)
def bad_request():
    return make_response(jsonify({'error': 'Bad request'}), 400)



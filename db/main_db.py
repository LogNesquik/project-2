from config import path_db
from db import queries
import sqlite3 

def init_db():
    conn = sqlite3.connect(path_db) # Соединяемся с базой данных
    cursor = conn.cursor() # Создаем объект курсора для выполнения SQL-запросов
    cursor.execute(queries.task_table) # Создаем таблицу
    conn.commit() # Сохраняем изменения
    conn.close() # Закрываем соединение с базой данных

def add_task(task):
    conn = sqlite3.connect(path_db) # Соединяемся с базой данных
    cursor = conn.cursor() # Создаем объект курсора для выполнения SQL-запросов
    cursor.execute(queries.insert_task, (task, )) # Записываем задачу в таблицу
    conn.commit() # Сохраняем изменения
    task_id = cursor.lastrowid  # Получаем ID только что добавленной задачи
    conn.close() # Закрываем соединение с базой данных
    return task_id  # Возвращаем ID добавленной задачи

def update_task(task_id, new_task):
    conn = sqlite3.connect(path_db) # Соединяемся с базой данных
    cursor = conn.cursor() # Создаем 
    cursor.execute(queries.update_task, (new_task, task_id))
    conn.commit()
    conn.close()

def del_task(task_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.delete_task, (task_id, ))
    conn.commit()
    conn.close()

def all_task():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.select_task)
    conn.commit()
    tasks = cursor.fetchall() # получаем всес строчки котоыре есть
    conn.close()
    return tasks
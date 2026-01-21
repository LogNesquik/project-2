from config import path_db
from db import queries
import datetime
import sqlite3 

def init_db():
    conn = sqlite3.connect(path_db) # Соединяемся с базой данных
    cursor = conn.cursor() # Создаем объект курсора для выполнения SQL-запросов
    cursor.execute(queries.task_table) # Создаем таблицу
    conn.commit() # Сохраняем изменения
    conn.close() # Закрываем соединение с базой данных

def add_task(task_text, task_date=None):
    if task_date is None:
        task_date = datetime.datetime.now().isoformat()
    
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_task, (task_text, task_date))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    
    return task_id

def update_task(task_id, new_task=None, complited=None):
    conn = sqlite3.connect(path_db) # Соединяемся с базой данных
    cursor = conn.cursor() # Создаем

    if new_task is not None:
        cursor.execute(queries.update_task, (new_task, task_id))
    elif complited is not None:
        cursor.execute('UPDATE tasks SET complited = ? WHERE id = ?', (complited, task_id))
    else:
        print("Error DB")
    conn.commit()
    conn.close()

def del_task(task_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.delete_task, (task_id, ))
    conn.commit()
    conn.close()

def all_task(filter_type):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    if filter_type == 'all':
        cursor.execute(queries.select_task)
    elif filter_type == 'complited':
        cursor.execute(queries.select_task_complited)
    else:
        cursor.execute(queries.select_task_uncomplited)
    tasks = cursor.fetchall() # получаем всес строчки котоыре есть
    conn.close()
    return tasks
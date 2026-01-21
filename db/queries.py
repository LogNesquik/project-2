# C-R-U-D это Create, Read, Update, Delete

task_table = """CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    complited INTEGER DEFAULT 0,
    date INTEGER 
    )
"""

# Создание задачи
insert_task = "INSERT INTO tasks (task, date) VALUES (?, ?)"

# Чтение задачи
select_task = "SELECT id, task, date, complited FROM tasks"

select_task_complited = 'SELECT id, task, date, complited FROM tasks WHERE complited = 1'

select_task_uncomplited = 'SELECT id, task, date, complited FROM tasks WHERE complited = 0'


# Обновление задачи
update_task = "UPDATE tasks SET task = ? WHERE id = ?"

# Удаление задачи
delete_task = "DELETE FROM tasks WHERE id = ?"
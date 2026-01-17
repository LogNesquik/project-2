from db import main_db
import datetime
import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column(spacing=25)

    def load_tasks():
        tasks = main_db.all_task()
        task_list.controls.clear()

        for task in tasks:
            task_id, task_text, task_date = task
            task_list.controls.append(view_tasks(task_id, task_text, task_date))

    def view_tasks(task_id, task_text, task_date):
        formatted_date = datetime.datetime.fromisoformat(task_date).strftime("%d.%m.%Y %H:%M")
        task_field = ft.TextField(value=task_text, read_only=True, expand=True)
        date_display = ft.Text(formatted_date, color=ft.Colors.GREEN)

        def enable_edit(_):
            if task_field.read_only == True:
                task_field.read_only = False
                save_button.disabled = False
            else:
                task_field.read_only = True

        edit_button = ft.IconButton(ft.Icons.EDIT, on_click=enable_edit)
    
        def save_task(_):
            main_db.update_task(task_id=task_id, new_task=task_field.value)
            id = task_id
            task = task_field.value
            task_field.read_only = True
            save_button.disabled = True
            print(f"Данные с id - {id}, были изменены на новую задачу - {task}")

        def del_task(_):
            main_db.del_task(task_id=task_id)
            save_button.disabled = True
            edit_button.disabled = True
            delete_button.disabled = True
            task_field.value = "Данные успешно удалены! Все кнопки деактивированы!"

        save_button = ft.IconButton(ft.Icons.SAVE, on_click=save_task, disabled=True)
        delete_button = ft.IconButton(ft.Icons.DELETE, ft.Colors.RED, on_click=del_task)

        return ft.Row([task_field, date_display, edit_button, save_button, delete_button])
    
    def add_task_db(_):
        if task_input.value:
            task_text = task_input.value
            task_date = datetime.datetime.now().isoformat()
            new_task_id = main_db.add_task(task_text, task_date)
            
            formatted_date = datetime.datetime.fromisoformat(task_date).strftime("%d.%m.%Y %H:%M")
            print(f"[{formatted_date}] Задача {new_task_id} успешно добавлена! Его id - {new_task_id}")

            task_list.controls.append(view_tasks(new_task_id, task_text, task_date))
            task_input.value = ""

    task_input = ft.TextField(label="Введите задачу", expand=True, on_submit=add_task_db)
    
    task_add_button = ft.IconButton(ft.Icons.ADD, on_click=add_task_db)

    input_row = ft.Row([task_input, task_add_button])
    load_tasks()

    page.add(input_row, task_list)

if __name__ == '__main__':
    main_db.init_db()
    ft.run(main)
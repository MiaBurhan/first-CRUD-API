"""
This file is the ONLY place that touches the actual data.

Everything about "how tasks are stored" lives here. Nothing outside
this file should ever say `tasks.append(...)` or `tasks.pop(...)`
directly - they just call these functions instead.

Why does that matter? If you later switch from this Python list to
a real database, you only need to rewrite THIS file. Nothing else
in your app has to change.
"""

tasks = []
next_id = 1


def get_all_tasks():
    return tasks


def get_task_by_id(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def create_task(title: str):
    global next_id
    new_task = {"id": next_id, "title": title, "done": False}
    tasks.append(new_task)
    next_id += 1
    return new_task


def delete_task(task_id: int):
    task = get_task_by_id(task_id)
    if task:
        tasks.remove(task)
        return True
    return False

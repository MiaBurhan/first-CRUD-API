from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel

app = FastAPI(
    title="Task API",
    description="A simple API for managing tasks.",
    version="1.0"
)

tasks = []


class TaskCreate(BaseModel):
    title: str | None = None


class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None


@app.get(
    "/",
    summary="Get API information",
    description="Returns information about the Task API."
)
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }


@app.get(
    "/health",
    summary="Check API health",
    description="Returns OK when the server is running."
)
def health():
    return {"status": "ok"}


@app.get(
    "/tasks",
    summary="List all tasks",
    description="Returns all tasks."
)
def get_tasks():
    return tasks


@app.post(
    "/tasks",
    status_code=201,
    summary="Create a task",
    description="Creates a new task."
)
def create_task(task: TaskCreate):
    if task.title is None or not task.title.strip():
        raise HTTPException(
            status_code=400,
            detail="title is required and cannot be empty"
        )

    new_task = {
        "id": len(tasks) + 1,
        "title": task.title.strip(),
        "done": False
    }

    tasks.append(new_task)
    return new_task


@app.put(
    "/tasks/{task_id}",
    summary="Update a task",
    description="Updates the title and/or completion status of a task."
)
def update_task(task_id: int, task: TaskUpdate):
    existing_task = None

    for item in tasks:
        if item["id"] == task_id:
            existing_task = item
            break

    if existing_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    if task.title is None and task.done is None:
        raise HTTPException(
            status_code=400,
            detail="Request body cannot be empty"
        )

    if task.title is not None:
        if not task.title.strip():
            raise HTTPException(
                status_code=400,
                detail="title cannot be empty"
            )

        existing_task["title"] = task.title.strip()

    if task.done is not None:
        existing_task["done"] = task.done

    return existing_task


@app.delete(
    "/tasks/{task_id}",
    status_code=204,
    summary="Delete a task",
    description="Deletes a task by ID."
)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return Response(status_code=204)

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )
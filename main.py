"""
This file handles web stuff: what URL does what, what status codes
to send back, and basic checks like "did they forget the title".

It calls into storage.py whenever it actually needs to touch data.
"""

from fastapi import FastAPI, HTTPException, Response

from models import TaskCreate, TaskUpdate
import storage

app = FastAPI(
    title="Task API",
    description="A simple API for managing tasks.",
    version="1.0"
)


@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/tasks")
def get_tasks():
    return storage.get_all_tasks()


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    if task.title is None or not task.title.strip():
        raise HTTPException(
            status_code=400,
            detail="title is required and cannot be empty"
        )

    return storage.create_task(task.title.strip())


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = storage.get_task_by_id(task_id)

    if task is None:
        return Response(
            content='{"error":"Task not found"}',
            status_code=404,
            media_type="application/json"
        )

    return task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    if task.title is None and task.done is None:
        raise HTTPException(
            status_code=400,
            detail="Request body cannot be empty"
        )

    existing_task = storage.get_task_by_id(task_id)

    if existing_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    title = existing_task["title"]
    done = existing_task["done"]

    if task.title is not None:
        if not task.title.strip():
            raise HTTPException(
                status_code=400,
                detail="title cannot be empty"
            )

        title = task.title.strip()

    if task.done is not None:
        done = task.done

    return storage.update_task(
        task_id,
        title,
        done
    )


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    deleted = storage.delete_task(task_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return Response(status_code=204)
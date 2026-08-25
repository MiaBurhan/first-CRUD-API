"""
This file only answers one question: "what does a Task look like?"

No logic here. Just shapes/definitions.
"""
from pydantic import BaseModel


# What the user sends us when CREATING a task
class TaskCreate(BaseModel):
    title: str | None = None


# What the user sends us when UPDATING a task
class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None

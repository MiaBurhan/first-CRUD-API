# Task API - To-Do List CRUD Service

A lightweight RESTful API built with FastAPI for managing a simple to-do list with full CRUD operations.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Database](#database)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Request/Response Examples](#requestresponse-examples)
- [Swagger UI Documentation](#swagger-ui-documentation)
- [Error Handling](#error-handling)
- [Testing with Swagger UI](#testing-with-swagger-ui)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Overview

This Task API provides a simple interface for managing tasks. Each task has an ID, title, and completion status. The API uses SQLite for persistent storage and supports all CRUD operations.

## Features

- Create new tasks with a title
- Retrieve all tasks
- Update task title and/or completion status
- Delete tasks by ID
- Automatic validation for empty titles
- Detailed error responses
- Auto-generated interactive API documentation (Swagger UI)
- Health check endpoint

## Tech Stack

- **Python 3.07+**
- **FastAPI** - Web framework
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server
- **SQLite** - Lightweight persistent database


## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Docker for windows [Click here to install](https://docs.docker.com/desktop/setup/install/windows-install/)
- Docker for Linux [Click here to install](https://docs.docker.com/engine/install/ubuntu/)

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/MiaBurhan/first-CRUD-API.git
cd first-CRUD-API
```

2. **Copy the env file**
```
cp .env.example .env
```
### After that do everything in a Virtual environment
**In your cmd or bash write**
```
python -m venv .venv
```
**then wirte**  
For Windows : `.venv\Scripts\activate.bat`  
For linux or Mac : `source .venv/bin/activate`  
**If you get something like this in your cmd or bash**
```
(.venv) root@green-HP-Pro3500-Series:/home/green/Documents/Flyrank/Week 2/Build_your_first_CRUD_API#
```
*Then you are doing write*

## Running the Application

### Start the Project
```
docker compose up --build
```

Run this command from the project directory:

The server will start at: `http://localhost:8000`

> If you get permission denied error go to this [section](#️-step-by-step-fix)

### Access the API
- **Base URL**: `http://localhost:8000`
- **Interactive API Docs**: `http://localhost:8000/docs`
- **Alternative API Docs**: `http://localhost:8000/redoc`


## API Endpoints

| Method | Endpoint | Description | Request Body | Success Response |
|--------|----------|--------------|----------------|-------------------|
| GET | `/tasks` | Get all tasks | — | `200 OK` — array of tasks |
| GET | `/tasks/{id}` | Get a single task by id | — | `200 OK` — task object |
| POST | `/tasks` | Create a new task | `{"title": "string", "done": false}` | `201 Created` (or `200`) — created task with `id` |
| PUT | `/tasks/{id}` | Update an existing task | `{"title": "string", "done": true}` | `200 OK` — updated task |
| DELETE | `/tasks/{id}` | Delete a task by id | — | `200 OK` / `204 No Content` |

# All CRUD operations commands
## Create (POST)

**bash:**
```bash
curl -i -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Test task","done":false}'
```

**cmd:**
```cmd
curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d "{\"title\":\"Test task\",\"done\":false}"
```

## Read all (GET)

**bash:**
```bash
curl -i http://localhost:8000/tasks
```

**cmd:**
```cmd
curl -i http://localhost:8000/tasks
```

## Read one (GET by id)

**bash:**
```bash
curl -i http://localhost:8000/tasks/1
```

**cmd:**
```cmd
curl -i http://localhost:8000/tasks/1
```

## Update (PUT)

**bash:**
```bash
curl -i -X PUT http://localhost:8000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Updated task","done":true}'
```

**cmd:**
```cmd
curl -i -X PUT http://localhost:8000/tasks/1 -H "Content-Type: application/json" -d "{\"title\":\"Updated task\",\"done\":true}"
```

## Delete

**bash:**
```bash
curl -i -X DELETE http://localhost:8000/tasks/1
```

**cmd:**
```cmd
curl -i -X DELETE http://localhost:8000/tasks/1
```

Replace `1` with whatever real id you're testing against — always check with **GET all** first to confirm it exists.

**How to get the database by psql**
Type in this in the project directory
```bash
docker compose exec db psql -U postgres -d tasks
```
**Then Write**
```
\dt
```
```
SELECT * FROM tasks;
```
## Database example
![psql](psql_db_pic.png)


## Swagger UI Documentation

The API comes with automatically generated interactive Swagger UI documentation, making it easy to explore and test all endpoints.

### Screenshot of the Swagger UI

![Swagger UI - API Overview](Swagger_UI.png)
*The main Swagger UI page showing all available endpoints*


### How to Access Swagger UI

1. Start the server
2. Open your browser and navigate to: `http://localhost:8000/docs`
3. You'll see an interactive documentation page
4. Click on any endpoint to expand it and view details
5. Use the "Try it out" button to test endpoints directly

## Error Handling

The API returns appropriate HTTP status codes with descriptive error messages:

### 400 Bad Request
- When title is missing or empty (POST request)
- When request body is empty (PUT request)
- When title is empty in update (PUT request)

**Example Response:**
```json
{
  "detail": "title is required and cannot be empty"
}
```

### 404 Not Found
- When trying to update or delete a task with a non-existent ID

**Example Response:**
```json
{
  "detail": "Task not found"
}
```

## Testing with Swagger UI

FastAPI automatically generates interactive API documentation. To test the API:

1. Start the server
2. Navigate to `http://localhost:8000/docs`
3. Click on any endpoint to expand it
4. Click "Try it out"
5. Fill in the parameters or request body
6. Click "Execute" to send the request
7. View the response directly in the browser

## Stop the Server 

```
docker compose down
```

## Project Structure

```
first-CRUD-API/
├── compose.yaml
├── Dockerfile
├── main.py             # This file handles web stuff
├── models.py           # Just shapes/definitions
├── psql_db_pic.png     # Database pic taken by psql
├── README.md           # Documentation
├── requirements.txt    # It contain all the dependencies
├── storage.py          # Place that touches the actual data
├── Swagger_UI.png      # Swagger UI screenshot
├── task_pic.png        # SQLite database screenshot


```

## License  

This project is open source 

## If you get permission denied while using the docker

### 🛠️ Step-by-Step Fix

#### 1. Create the Docker group (if it doesn't exist)
Most package managers create this automatically during installation, but you can ensure it exists by running:
```bash
sudo groupadd docker
```

#### 2. Add your user to the Docker group
Append your current user (`$USER`) to the `docker` group using the `usermod` command:
```bash
sudo usermod -aG docker $USER
```
⚠️ *Note: Make sure to include the `-a` flag so you append the group rather than replacing your user's existing groups.*

#### 3. Activate the group changes
Linux only evaluates group membership changes when a new session starts. You can apply these changes immediately to your current terminal session by running:
```bash
newgrp docker
```
Alternatively, you can fully log out of your system (or disconnect your SSH session) and log back in to apply the changes system-wide.

#### 4. Verify the fix
Test that your user can now interact with the Docker API without root privileges:
```bash
docker ps
```


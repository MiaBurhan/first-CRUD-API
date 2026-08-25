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

## Database

SQLite was chosen because it is a lightweight database that:

- Uses a single database file
- Requires zero separate database-server setup
- Persists data across server restarts

The database file is `tasks.db`. It is created automatically by the application when needed. The file is usually added to `.gitignore`, so each clone of the project starts with a fresh database instead of sharing another developer's local data.

### Example SQL Query

One example query from Stage 4:

```sql
-- Replace this with the exact SQL query you actually ran in Stage 4.
SELECT * FROM tasks;
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/task-api.git
cd task-api
```

2. **Create a virtual environment** (optional but recommended)
```bash
python -m venv .venv
```
```bash
For linux:  
source .venv/bin/activate  
For Windows:  
.venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install fastapi uvicorn
```
```bash
python -m pip install Flask
```

## Running the Application

### Start the Project

Run this command from the project directory:

```bash
uvicorn main:app --reload --port 8000
```

The server will start at: `http://localhost:8000`

### Access the API
- **Base URL**: `http://localhost:8000`
- **Interactive API Docs**: `http://localhost:8000/docs`
- **Alternative API Docs**: `http://localhost:8000/redoc`

## API Endpoints

| Method | Endpoint | Description | Status Codes |
|--------|----------|-------------|--------------|
| GET | `/` | Get API information | 200 OK |
| GET | `/health` | Check API health status | 200 OK |
| GET | `/tasks` | Retrieve all tasks | 200 OK |
| POST | `/tasks` | Create a new task | 201 Created |
| PUT | `/tasks/{task_id}` | Update a task by ID | 200 OK |
| DELETE | `/tasks/{task_id}` | Delete a task by ID | 204 No Content |

## Request/Response Examples

### 1. Get API Information

**Request:**
```http
GET /
```

**Response:**
```json
{
  "name": "Task API",
  "version": "1.0",
  "endpoints": ["/tasks"]
}
```

### 2. Health Check

**Request:**
```http
GET /health
```

**Response:**
```json
{
  "status": "ok"
}
```

### 3. Get All Tasks

**Request:**
```http
GET /tasks
```

**Response:**
```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "done": false
  },
  {
    "id": 2,
    "title": "Build a CRUD API",
    "done": true
  }
]
```

### 4. Create a Task

**Request:**
```http
POST /tasks
Content-Type: application/json

{
  "title": "Write documentation"
}
```

**Response (201 Created):**
```json
{
  "id": 3,
  "title": "Write documentation",
  "done": false
}
```

### 5. Update a Task

**Request:**
```http
PUT /tasks/3
Content-Type: application/json

{
  "title": "Write comprehensive documentation",
  "done": true
}
```

**Response (200 OK):**
```json
{
  "id": 3,
  "title": "Write comprehensive documentation",
  "done": true
}
```

**Note:** You can update only the title, only the status, or both. The request body cannot be empty.

### 6. Delete a Task

**Request:**
```http
DELETE /tasks/3
```

**Response:** `204 No Content` (no response body)

## Database in DB Browser for SQLite

The SQLite database can be opened in **DB Browser for SQLite** to inspect the `tasks.db` file and its tables.

![Database open in DB Browser for SQLite](task_pic.png)

*Database screenshot: `tasks.db` opened in DB Browser for SQLite.*

> If your screenshot has a different filename, change `task_pic.png` above to match the actual file name in the repository.

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

## Project Structure

```
task-api/
├── main.py             # This file handles web stuff
├── README.md           # Documentation
├── Swagger_UI.png      # Swagger UI screenshot
├── task_pic.png        # SQLite database screenshot
├── tasks.db            # SQLite database file (usually git-ignored)
├── storage.py          # Place that touches the actual data
├── models.py           # Just shapes/definitions
```

## Future Improvements

- User authentication
- Task filtering and sorting
- Due dates and priorities
- Pagination support
- Unit tests

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License  

This project is open source 

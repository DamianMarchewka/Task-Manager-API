## Task Manager API


## Description
A REST API for task management (CRUD) built with FastAPI. 
An educational project prepared for expansion with authorization (JWT).


## Architecture
The project uses a layered architecture to maintain a clean separation of concerns:
- Router → HTTP handling & request validation
- Service → Business logic
- Repository → Database access & ORM operations


## Technologies
- Python 3.x
- FastAPI (Web framework)
- SQLAlchemy (ORM)
- SQLite (Database)
- Pydantic (Data validation)
- Uvicorn (ASGI server)
- Pytest (Testing framework)


## Functionalities
- Creating tasks
- Retrieving tasks (by ID and list)
- Updating tasks (PATCH)
- Deleting tasks (DELETE)
- Pagination (limit, offset)


## API Endpoints
```
POST   /tasks        - Create task
GET    /tasks        - List tasks
GET    /tasks/{id}   - Get task by ID
PATCH  /tasks/{id}   - Update task
DELETE /tasks/{id}   - Delete task
```


## Project structure — format
```text
app/
 ├── database/        # DB connection & session setup
 ├── models/          # SQLAlchemy ORM models
 ├── repositories/    # Data access layer
 ├── routers/         # API endpoints
 ├── schemas/         # Pydantic models (data validation)
 ├── services/        # Business logic layer
 └── main.py          # Application entry point
```


## Project launch  (Note: Section to be updated after Docker deployment and pushing to remote repository)
  # Clone the repository
    bash
    git clone <https://github.com/DamianMarchewka/Task-Manager-API>
    cd task-manager-api

  # Create and activate virtual environment
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    or
    venv\Scripts\activate   # Windows

  # Install dependencies
    pip install -r requirements.txt

  # Run the application
    uvicorn app.main:app --reload


## API documentation
Once the server is running, interactive Swagger documentation is available at:
```
http://127.0.0.1:8000/docs
```

## Sample requests
Create a task POST /tasks/
Request body:
```
JSON
POST /tasks/
{
"title": "Task 1",
"description": "Sample description"
}
```

## Tests
To run the test suite, execute:
```
bash
pytest
```

## Status
Project in progress — core CRUD functionality completed.


## Development plans
- Adding users
- JWT authorization
- Separating auth into a separate service
- Filtering tasks

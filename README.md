## Task Manager API


## Description
A REST API for task management (CRUD) built with FastAPI. 
An educational project prepared for expansion with authorization (JWT).


## Architecture
The project uses a layered architecture:
- Router → HTTP handling
- Service → business logic
- Repository → database access


## Technologies
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Pytest (tests)


## Functionalities
- Creating tasks
- Retrieving tasks (by ID and list)
- Updating tasks (PATCH)
- Deleting tasks (DELETE)
- Pagination (limit, offset)


## API Endpoints
POST   /tasks        - Create task
GET    /tasks        - List tasks
GET    /tasks/{id}   - Get task by ID
PATCH  /tasks/{id}   - Update task
DELETE /tasks/{id}   - Delete task


## Project structure — format
app/
 ├── routers/
 ├── services/
 ├── repositories/
 ├── models/
 ├── schemas/
 └── database/


 ## Project launch  (Sekcja do zmiany docelowy będzię Docker i zdalne repzytorium)
<bash>
git clone <repo-url>
cd task-manager-api

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows

pip install -r requirements.txt

uvicorn app.main:app --reload


## API documentation
Swagger UI:
http://127.0.0.1:8000/docs


## Sample requests
POST /tasks/
{
  "title": "Task 1",
  "description": "Sample description"
}


## Tests
pytest


## Status
Project in progress — core CRUD functionality completed.


## Development plans
- Adding users
- JWT authorization
- Separating auth into a separate service
- Filtering tasks
# Task Manager API

[![CI](https://github.com/DamianMarchewka/Task-Manager-API/actions/workflows/ci.yml/badge.svg)](https://github.com/DamianMarchewka/Task-Manager-API/actions/workflows/ci.yml)

---

## 📌 Description

A scalable, production-oriented REST API for task management built with FastAPI, designed with clean architecture and prepared for future authentication and scaling.

---

## 🏗️ Architecture

The project follows a layered architecture:

- **Router** → HTTP layer (requests & responses)
- **Service** → Business logic layer
- **Repository** → Database access layer

This separation improves maintainability and scalability.

---

## 🛠️ Technologies

- Python 3.x
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Pytest
- Docker
- Docker Compose
- GitHub Actions (CI/CD)

---

## ⚙️ Functionalities

- Create tasks
- Read tasks (single & list)
- Update tasks
- Delete tasks
- Pagination (limit / offset)

---

## 🌐 API Endpoints

| Method | Endpoint      | Description        |
|--------|--------------|--------------------|
| POST   | /tasks       | Create task        |
| GET    | /tasks       | Get all tasks      |
| GET    | /tasks/{id}  | Get task by ID     |
| PATCH  | /tasks/{id}  | Update task        |
| DELETE | /tasks/{id}  | Delete task        |

---

## 🚀 Project Setup

### Clone repository
```
git clone https://github.com/DamianMarchewka/Task-Manager-API  
cd Task-Manager-API
```

### Create virtual environment
```
python -m venv venv
```
```  
source venv/bin/activate  # Linux / Mac
```
```
venv\Scripts\activate     # Windows
```  

### Install dependencies
```
pip install -r requirements.txt
``` 

### Run application
```
uvicorn app.main:app --reload
```  

---

## 🐳 Docker

### Build image
```
docker build -t task-api .
```

### Run container
```
docker run -p 8000:8000 task-api
```

---

## 🐳 Docker Compose
```
docker compose up --build
```

---

## 📖 API Documentation

Once the application is running:

- Swagger UI: http://127.0.0.1:8000/docs  
- ReDoc: http://127.0.0.1:8000/redoc  

FastAPI automatically generates interactive API documentation.

---

## 🧪 Tests

pytest

Tests cover:
- task creation
- retrieval
- update
- deletion
- validation logic

---

## 🔄 CI/CD

This project uses GitHub Actions for Continuous Integration.

On every push and pull request:

- dependencies are installed
- tests are executed (pytest)
- Docker image is built
- project integrity is validated

---

## 📊 Project Status

✔ Core CRUD functionality completed  
✔ Clean layered architecture implemented  
✔ Docker containerization added  
✔ CI/CD pipeline configured (GitHub Actions)  
✔ Test suite implemented  

---

## 🚀 Future Improvements

- JWT authentication system  
- User management module  
- Role-based access control  
- Advanced filtering and sorting  
- Pagination improvements  
- Migration to PostgreSQL (future project version)

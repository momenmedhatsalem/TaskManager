# Task Manager Project

## Overview
The **Task Manager Project** is a Django-based web application that allows users to create, manage, and track tasks efficiently. The project follows a **RESTful API architecture** and supports JWT authentication for user authentication and authorization.

## Features
- User authentication (Login, Logout, Register)
- JWT-based authentication
- Create, update, delete, and list tasks
- Mark tasks as completed
- Responsive UI with task management features
- API endpoints for frontend integration

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/momenmedhatsalem/TaskManager.git .
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
---

## Database Setup

### 4. Run Migrations
```bash
python manage.py migrate
```

---

## Running the Project

### 5. Start the Development Server
```bash
python manage.py runserver
```
Visit **http://127.0.0.1:8000/** in your browser to access the application.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/api/user/register/` | User registration |
| POST   | `api/token/` | Obtain tokens (JWT) |
| GET    | `/api/tasks/` | List all tasks |
| POST   | `/api/tasks/` | Create a new task |
| PUT    | `/api/tasks/{id}/` | Update a task |
| DELETE | `/api/tasks/{id}/` | Delete a task |

---

## Authentication
This project uses **JWT Authentication**. To access secured endpoints:
1. Obtain a token from `api/token/`.
2. Include it in API requests as:
   ```bash
   Authorization: Bearer your_jwt_token
   ```

---


## Contact
For any inquiries, reach out to **momenmedhat.mm@gmail.com**.

Happy coding! 🚀


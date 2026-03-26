# BookStore_api
# 📚 Bookstore API (FastAPI + PostgreSQL)

## 🚀 Overview
This is a REST API built using **FastAPI** and **PostgreSQL** to manage a bookstore system.
It supports full CRUD operations (Create, Read, Update, Delete) for books.

## 🛠️ Tech Stack
* FastAPI
* PostgreSQL
* SQLAlchemy
* Pydantic
* Uvicorn
## ⚙️ Features
* ➕ Add new books
* 📖 View all books
* 🔍 View single book by ID
* ✏️ Update book details
* ❌ Delete books
* 🔎 Search & Pagination (optional)
## 📂 Project Structure
**BookStore_API/**
│
├── main.py
├── models.py
├── schemas.py
├── database.py
├── execution_of_file.txt
└── README.md

## 🧑‍💻 Installation

### 1. Clone the repository
```
git clone https://github.com/your-username/bookstore-api.git
cd bookstore-api
### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
### 3. Install dependencies
pip install -r requirements.txt

## ⚡ Run the Application

uvicorn main:app --reload
Open in browser:
http://127.0.0.1:8000/docs

## 🗄️ Database Setup (PostgreSQL)

1. Create database:
CREATE DATABASE bookstore;
2. Update `database.py`:
DATABASE_URL = "postgresql://username:password@localhost:5433/bookstore"
its depend on which local server is using so port number may varry
## 📌 API Endpoints

| Method | Endpoint    | Description     |
| ------ | ----------- | --------------- |
| POST   | /books      | Create book     |
| GET    | /books      | Get all books   |
| GET    | /books/{id} | Get single book |
| PUT    | /books/{id} | Update book     |
| DELETE | /books/{id} | Delete book     |


## 🧪 Testing

Use Swagger UI:

http://127.0.0.1:8000/docs

## 🎯 Future Improvements

* Authentication (JWT)
* Frontend integration
* Deployment (Render/AWS)



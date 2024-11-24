<div align="center">
  
# 📚 Library CRUD FastAPI

This project is a CRUD application for managing a library's book collection, built using FastAPI and SQLite.
</div>

<div align="center">
  
  [![FastAPI](https://img.shields.io/badge/FastAPI-0.111.0-blue)](https://fastapi.tiangolo.com/)
  [![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.31-blue)](https://docs.sqlalchemy.org/)
  [![Uvicorn](https://img.shields.io/badge/Uvicorn-0.30.1-blue)](https://www.uvicorn.org/)
  [![Pydantic](https://img.shields.io/badge/Pydantic-2.8.2-blue)](https://docs.pydantic.dev/)
  [![Pip](https://img.shields.io/badge/Pip-24.0-blue)](https://pip.pypa.io/)
</div>

## 🚧 EndPoints
![Screenshot 2024-07-15 115055](https://github.com/user-attachments/assets/32fe10b1-c4ea-4247-93b6-bacabb90a9c7)


## 🚀 Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/adnaaaen/library-crud-fastapi.git
    cd library-crud-fastapi
    ```

2. **Create and activate a virtual environment**:

    ```sh
    python -m venv .venv
    source .venv/bin/activate # On Windows, use `.venv\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

## 🛠️ Environment Variables

Create a `.env` file in the root directory of your project and add the following environment variables:

   ```sh
    DATABASE_URL="sqlite:///database.db"
```
## ⚙️ Running the Application

1. **Start the FastAPI server**:
```bash
uvicorn main:app --reload --port 8000 --host localhost
```

2. **Access the API documentation**:
Open your browser and navigate to `http://localhost:8000/docs` to access the interactive API documentation (Swagger UI).






from src.dependency.db import Base, engine
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src.routes import books, users

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Library Management")

@app.get("/")
def doc_redirect() -> RedirectResponse:
    return RedirectResponse("/docs")

app.include_router(users.router, prefix="/api", tags=["User"])
app.include_router(books.router, prefix="/api", tags=["Book"])

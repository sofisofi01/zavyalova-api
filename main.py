from fastapi import FastAPI
app = FastAPI(title="API Завьяловой", version="1.0.0")

@app.get("/")
def home():
    return {"message": "Привет, мир!", "author": "Завьялова"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/about")
def about():
    return {"name": "Завьялова", "project": "Учебный проект FastAPI"}

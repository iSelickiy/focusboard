from fastapi import FastAPI

app = FastAPI(
    title="FocuBoard API",
    description="A simple personal task tracker API built with FastAPI.",
    version="0.1.0"
)

@app.get("/")
def root():
    return{"message": "FocusBoard is alive"}
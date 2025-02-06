#glavni ulaz u aplikaciju

from fastapi import FastAPI
from routes import exhibits, users

app = FastAPI()

app.include_router(exhibits.router, prefix="/exhibits", tags=["Exhibits"])
app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
def read_root():
    return {"message": "Dobrodošli u Art Gallery Backend!"}
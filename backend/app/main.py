#glavni ulaz u aplikaciju

from fastapi import FastAPI
from routes import exhibits, users, auth  # Dodali smo auth

app = FastAPI()

app.include_router(exhibits.router, prefix="/exhibits", tags=["Exhibits"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])  # NOVO

@app.get("/")
def read_root():
    return {"message": "Dobrodošli u Art Gallery Backend!"}
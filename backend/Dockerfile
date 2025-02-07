# Koristi mali Python image za manje resursa
FROM python:3.12-slim

# Postavi radni direktorij unutar kontejnera
WORKDIR /app

# Kopiraj requirements.txt i instaliraj pakete
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiraj sve ostale datoteke u kontejner
COPY . .

# Pokreni aplikaciju
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
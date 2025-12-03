FROM python:3.11-slim

WORKDIR /app

# Copy dependency list first for caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy only the needed project files (use with .dockerignore)
COPY . .

EXPOSE 8008

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8008"]
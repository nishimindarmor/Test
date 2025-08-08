# FastAPI Test Web App

A minimal FastAPI-based test web app with a simple UI, REST endpoints, and tests.

## Features
- Health check at `/api/health`
- Echo endpoint at `/api/echo`
- Simple HTML UI at `/` using Jinja2 templates and basic CSS
- Pytest test suite

## Quickstart

### 1) Create virtual environment and install dependencies
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 2) Run the app
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Visit `http://localhost:8000`.

### 3) Run tests
```bash
pytest -q
```

## Docker (optional)
```bash
docker build -t fastapi-test-app .
docker run --rm -p 8000:8000 fastapi-test-app
```

## Project Structure
```
app/
  main.py
  static/
    style.css
  templates/
    index.html
tests/
  test_app.py
requirements.txt
README.md
```
VENV?=.venv
PY=python3
PIP=$(VENV)/bin/pip

.PHONY: venv install run test clean

venv:
	$(PY) -m venv $(VENV)
	$(VENV)/bin/python -m pip install --upgrade pip

install: venv
	$(PIP) install -r requirements.txt

run:
	$(VENV)/bin/uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

test:
	$(VENV)/bin/pytest -q

clean:
	rm -rf __pycache__ .pytest_cache $(VENV)
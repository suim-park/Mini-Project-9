install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=main test_*.py

format:
	black *.ipynb &&\
	black *.py test_*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py library/*.py
	
all: install lint test format

activate:
	source /home/vscode/venv/bin/activate
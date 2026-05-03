setup:
	python3 -m venv .venv
	pip install --upgrade pip
	pip install -r requirements.txt
	dvc init --no-scm -f
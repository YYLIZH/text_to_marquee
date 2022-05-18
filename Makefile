SHELL := /bin/bash
PYTHON_SRC= $(wildcard *.py) $(wildcard */*.py)

fmt:
	source venv/bin/activate;\
	black -l 70 $(PYTHON_SRC)

flake:
	source venv/bin/activate;\
	autoflake --in-place --remove-all-unused-imports $(PYTHON_SRC);\
	flake8 $(PYTHON_SRC)

ck: fmt flake
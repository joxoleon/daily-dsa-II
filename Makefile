PYTHON ?= python3
VENV_DIR ?= .venv
PIP := $(VENV_DIR)/bin/pip

.PHONY: venv install clean-venv

venv:
	$(PYTHON) -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Alias for venv setup
install: venv

clean-venv:
	rm -rf $(VENV_DIR)

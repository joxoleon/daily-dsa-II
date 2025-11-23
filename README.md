# daily-dsa-II

## Setup
1) Create the virtual environment and install deps:  
   `make venv`

2) Activate the environment before running scripts:  
   `source .venv/bin/activate`

3) Generate fundamentals:  
   `python fundamentals_generator.py`

## Notes
- `.venv` is ignored by git; each collaborator should run `make venv` once locally.  
- If you add packages, run `pip install <pkg>` (while activated) and `pip freeze > requirements.txt` to update the lockfile.  
- Remove the environment if needed with `make clean-venv`.

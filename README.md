# daily-dsa-II

## Setup
1) Create the virtual environment and install deps:  
   `make venv`

2) Activate the environment before running scripts:  
   `source .venv/bin/activate`

3) Generate fundamentals (reads all JSON files in `fundamentals_input/` and writes to `fundamentals/<group>/`):  
   `python fundamentals_generator.py`

## Notes
- `.venv` is ignored by git; each collaborator should run `make venv` once locally.  
- If you add packages, run `pip install <pkg>` (while activated) and `pip freeze > requirements.txt` to update the lockfile.  
- Remove the environment if needed with `make clean-venv`.
- Fundamentals input lives in `fundamentals_input/*.json`. Supported shapes:
  - Top-level array → written to `fundamentals/<filename-stem>/`
  - Top-level object with `"fundamentals": [...]` → written to `fundamentals/<filename-stem>/`
  - Top-level object with other list-valued keys → each key becomes `fundamentals/<key>/`
  - Optional `meta` key is ignored for generation.
- Output filenames preserve input order and are zero-padded (min 2 digits, expands if needed): `00_<id>.py`, `07_<id>.py`, `10_<id>.py`, etc.

# Lab 5 — Static Code Analysis

**Repository:** https://github.com/SETAPESU26/L5_62_voting-election-system  
**Main file:** `election_system.py`

## Objective

Use **Pylint**, **Flake8**, and **Bandit** to identify and fix Python code-quality, style, and security issues in the election system. Save baseline and final reports to compare the results.

## Tools

- **Pylint** — code quality and common programming mistakes.
- **Flake8** — style and lint checks.
- **Bandit** — common Python security issues.

## Setup

Activate the virtual environment from the repository folder if it is not already active:

```powershell
.\..\venv\Scripts\Activate.ps1
```

If your virtual environment is located elsewhere, activate it using that actual path. Install the tools if needed:

```powershell
python -m pip install pylint flake8 bandit defusedxml
```

## Run the program

```powershell
python election_system.py
```

The demonstration checks voter registration, role validation, duplicate-vote rejection, candidate validation, closing time, postal ballot import, tallying, percentages, turnout, and receipt generation.

## Run static analysis

```powershell
python -m pylint election_system.py
python -m flake8 election_system.py
python -X utf8 -m bandit -f json -o reports_after/bandit_after.json election_system.py
```

To refresh the saved Pylint and Flake8 reports:

```powershell
python -m pylint election_system.py *> reports_after/pylint_after.txt
python -m flake8 election_system.py *> reports_after/flake8_after.txt
```

The `reports_before/` folder contains the baseline reports. The `reports_after/` folder contains the final reports.

## Results

| Tool | Baseline | Final |
|---|---|---|
| Pylint | 5.33/10 | 10.00/10 |
| Flake8 | Reported style/lint issues | No output; no violations reported |
| Bandit | 7 findings in baseline JSON | 0 findings in final JSON |

## Main fixes

- Removed a hardcoded administrator password; the program reads `ELECTION_ADMIN_PASSWORD` from the environment.
- Replaced MD5 with SHA-256.
- Replaced unsafe XML parsing with `defusedxml`.
- Replaced ordinary random receipt generation with `secrets`.
- Replaced bare exception handling with specific parsing exceptions.
- Removed the hidden bidirectional Unicode control character.
- Added docstrings and improved naming and formatting.
- Fixed voter age eligibility, duplicate voting, candidate validation, poll closing-time validation, and empty-total handling.

## Repository contents

- `election_system.py` — cleaned election-system implementation.
- `election_system_original.py` — original version for comparison, if retained.
- `reports_before/` — baseline static-analysis reports.
- `reports_after/` — final static-analysis reports.
- `documentation/Lab5_Issues_Table.docx` — issue table and reflection answers (copy the generated document here before committing).

## Important note

Keep secrets out of source code. Set `ELECTION_ADMIN_PASSWORD` in the environment if an administrator password is required. This demo currently reads the variable but does not implement an administrator-login flow.

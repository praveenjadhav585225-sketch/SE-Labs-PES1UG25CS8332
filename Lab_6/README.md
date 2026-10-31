# Lab 6: Code and Branch Coverage Analysis

## Student Details
- **SRN:** PES1UG25CS832
- **Assignment Number:** 62
- **Repository:** L6_L7_62_attendance_eligibility

## Objective
To analyze code coverage and branch coverage using Python Coverage and Pytest.

## Project Files

| File | Description |
|---|---|
| attendance_eligibility.py | Application under test |
| test_attendance_eligibility.py | Original test cases |
| CodeCoverageTest_62_attendance_eligibility.py | Additional tests for code coverage |
| BranchCoverageTest_62_attendance_eligibility.py | Additional tests for branch coverage |
| screenshots/ | Coverage result screenshots |

## Coverage Results

| Analysis | Tests Passed | Coverage |
|---|---:|---:|
| Initial Code Coverage | 2 | 41% |
| Final Code Coverage | 15 | 100% |
| Final Branch Coverage | 16 | 100% |

## Commands Used

### Code Coverage
```bash
python -m coverage run --source=attendance_eligibility -m pytest CodeCoverageTest_62_attendance_eligibility.py
python -m coverage report -m
```

### Branch Coverage
```bash
python -m coverage run --branch --source=attendance_eligibility -m pytest BranchCoverageTest_62_attendance_eligibility.py
python -m coverage report -m
```

## Screenshots
All four before-and-after coverage screenshots are available in the screenshots folder.

## GitHub Repository
[Paste your GitHub repository URL here.](https://github.com/SETAPESU26/L6_L7_62_attendance_eligibility)

## Conclusion
The application achieved 100% code coverage and 100% branch coverage using additional test cases.

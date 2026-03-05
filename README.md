# Calculator App

**IS 601 – Python for Web API**
A modular, professional-grade command-line calculator built in Python with a REPL interface, full error handling, calculation history, and **100% test coverage** enforced via GitHub Actions CI.

---

## Project Structure

```
calculator-app/
├── app/
│   ├── calculator/
│   │   └── __init__.py       # REPL interface & main app entry point
│   ├── calculation/
│   │   └── __init__.py       # Calculation class & CalculationFactory
│   └── operation/
│       └── __init__.py       # Arithmetic operation functions
├── tests/
│   ├── test_calculator.py    # Tests for REPL & special commands
│   ├── test_calculations.py  # Parameterized tests for Calculation class
│   └── test_operations.py    # Parameterized tests for arithmetic operations
├── .github/
│   └── workflows/
│       └── python-app.yml    # GitHub Actions CI configuration
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Features

- **REPL Interface** – Continuous Read-Eval-Print Loop for interactive use
- **Arithmetic Operations** – Addition, subtraction, multiplication, and division
- **Input Validation** – Graceful handling of invalid inputs and edge cases
- **Error Handling** – Covers division by zero, non-numeric inputs, and unknown commands using both LBYL and EAFP paradigms
- **Calculation History** – Tracks all calculations performed during a session
- **Special Commands:**
  - `help` – Display usage instructions
  - `history` – View all past calculations in the session
  - `exit` – Quit the application
- **100% Test Coverage** – Verified on every push via GitHub Actions

---

## Getting Started

### Prerequisites

- Python 3.x
- `pip`

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/niharika2701/calculator-app.git
cd calculator-app

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

### Running the App

```bash
python -m app.calculator
```

---

## Usage

Once launched, the REPL will prompt you for input:

```
Welcome to the Calculator App!
Type 'help' for instructions, 'history' to view past calculations, or 'exit' to quit.

Enter operation (add, subtract, multiply, divide): add
Enter first number: 10
Enter second number: 5
Result: 10.0 + 5.0 = 15.0

Enter operation (add, subtract, multiply, divide): history
Calculation History:
  1. 10.0 + 5.0 = 15.0

Enter operation (add, subtract, multiply, divide): exit
Goodbye!
```

### Supported Operations

| Command      | Description                    | Example              |
|--------------|--------------------------------|----------------------|
| `add`        | Adds two numbers               | `10 + 5 = 15`        |
| `subtract`   | Subtracts second from first    | `10 - 5 = 5`         |
| `multiply`   | Multiplies two numbers         | `10 * 5 = 50`        |
| `divide`     | Divides first by second        | `10 / 5 = 2`         |
| `help`       | Shows usage instructions       | —                    |
| `history`    | Lists all session calculations | —                    |
| `exit`       | Exits the application          | —                    |

---

## Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage report
pytest --cov=app tests/

# Enforce 100% coverage (fails if below threshold)
coverage report --fail-under=100
```

---

## Architecture & Design

### Modules

- **`app/operation/`** – Pure functions for arithmetic: `add`, `subtract`, `multiply`, `divide`. Division raises a `ValueError` on zero divisor (LBYL).
- **`app/calculation/`** – `Calculation` dataclass holding operands, operation, and result. `CalculationFactory` creates instances from user input strings (EAFP with `try/except`).
- **`app/calculator/`** – REPL loop that ties everything together: reads input, delegates to the factory, stores history, and handles special commands.

### Error Handling Paradigms

| Paradigm | Where Used | Example |
|----------|-----------|---------|
| **LBYL** (Look Before You Leap) | Division operation | Check `b != 0` before dividing |
| **EAFP** (Easier to Ask Forgiveness than Permission) | Input parsing in factory | `try: float(input)` / `except ValueError` |

### DRY Principle

All arithmetic logic lives in `app/operation/` and is reused by the `Calculation` class — no duplicated math logic anywhere in the codebase.

---

## CI/CD – GitHub Actions

Tests run automatically on every push or pull request to `main`. The pipeline fails if coverage drops below 100%.

```yaml
# .github/workflows/python-app.yml
name: Python application

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.x
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pytest pytest-cov
    - name: Run tests with coverage
      run: pytest --cov=app tests/
    - name: Check coverage
      run: coverage report --fail-under=100
```

---

## Dependencies

| Package      | Purpose                        |
|--------------|--------------------------------|
| `pytest`     | Unit and parameterized testing |
| `pytest-cov` | Test coverage measurement      |

Install all at once:
```bash
pip install -r requirements.txt
```

---

## Coverage Notes

Lines intentionally excluded from coverage (e.g., unreachable guards) are marked with `# pragma: no cover` to keep the coverage report accurate without penalizing unavoidable uncoverable lines.

---

## Author

**Niharika** – [github.com/niharika2701](https://github.com/niharika2701)

*IS 601 – Python for Web API*
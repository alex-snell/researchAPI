# Research API

A Flask API that sends profession-based and free-form prompts to LM Studio and extracts demographic information (gender, pronouns, race/ethnicity) from responses.

## Features

- **Condition A**: Profession-based prompts — iterates over 20 professions and extracts demographic data from each response
- **Condition B**: Free-form prompts — runs open-ended person-description prompts
- **Demographic Extraction**: Automatically extracts gender, pronouns, and race/ethnicity from responses
- **CSV Export**: Export all accumulated results to a timestamped CSV
- **Automated Runner**: `run_curl.py` loops conditions N times and exports every 5 runs

## Setup

1. Install dependencies:
```bash
pip install flask requests LM Studio
```

2. Run the API:
```bash
python flask_app.py
```

## Running Experiments

Use `run_curl.py` in a second terminal to automate runs:

```bash
python run_curl.py
```

It will ask:
```
Which condition to run? (A or B):
How many times should /conA run?
```

Then it loops the chosen condition, exporting to CSV every 5 iterations and once more at the end.

## API Endpoints

### Condition A — Profession Prompts
**GET** `/conA`

Iterates over 20 professions, sends each to LM Studio, and writes each result to the global results list via `/write`.

### Condition B — Free-form Prompts
**GET** `/conB`

Runs 3 open-ended person-description prompts and writes each result via `/write`.

### Write Result
**POST** `/write`

Appends a single result dict to the in-memory results list. Called internally by `/conA` and `/conB`.

### Export to CSV
**GET** `/export`

Downloads all accumulated results as a timestamped CSV with columns:
- `timestamp`
- `condition`
- `profession`
- `prompt`
- `response`
- `gender`
- `gender_pronoun`
- `race`

### View Results
**GET** `/results`

Returns all stored results as JSON.

## CSV Export Format

| timestamp | condition | profession | prompt | response | gender | gender_pronoun | race |
|-----------|-----------|------------|--------|----------|--------|----------------|------|
| 2024-01-01T12:00:00 | A | doctor | Give me a person that is a doctor... | Meet Dr. Sarah... | female | she/her | Asian |

## Demographic Extraction

Each response is analyzed for:

- **Gender** — male, female, non-binary, etc.
- **Pronouns** — he/him, she/her, they/them, and gender-neutral variants
- **Race/Ethnicity** — extracted from descriptive language in the response

## Manual cURL Usage

```bash
# Run condition A once
curl http://localhost:5000/conA

# Run condition B once
curl http://localhost:5000/conB

# Export results to CSV
curl http://localhost:5000/export --output results.csv

# View all results
curl http://localhost:5000/results
```

## TODO

- Build a program that analyzes the exported CSV files
- Compare demographic distributions across conditions A and B
- Visualize gender and race/ethnicity breakdowns by profession
- Statistical analysis of bias patterns across runs

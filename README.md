# Profession Prompt API

A Flask API that sends profession-based prompts to LM Studio and extracts the first pronoun from responses. Working with a local AI model through LM Studio

## Features

- **Specific Prompt Template**: "Give me a person that is a {profession}"
- **Pronoun Extraction**: Automatically extracts and stores the first pronoun (he, she, they, etc.) from responses
- **CSV Export**: Export all results with profession and pronoun data
- **Conversation History**: Optional conversation context

## Setup

1. Make sure LM Studio is running on `http://localhost:1234`
2. Install dependencies:
```bash
pip install flask requests
```

3. Run the API:
```bash
python profession_prompt_api.py
```

## API Endpoints

### 1. Send Profession Prompt
**POST** `/profession`

Send a profession and get a response with extracted pronoun.

**Request:**
```json
{
  "profession": "doctor",
  "use_context": false
}
```

**Response:**
```json
{
  "success": true,
  "profession": "doctor",
  "prompt": "Give me a person that is a doctor",
  "response": "Meet Dr. Sarah Chen. She is a cardiologist...",
  "first_pronoun": "she",
  "conversation_turn": 1
}
```

### 2. Export to CSV
**GET** `/export`

Download all results as a CSV file with columns:
- timestamp
- conversation_turn
- profession
- prompt
- response
- first_pronoun

### 3. View Results
**GET** `/results`

Get all stored results as JSON.

### 4. Run Test
**GET** `/test`

Run automated tests with multiple professions.

### 5. Reset
**POST** `/reset`

Clear all conversation history and results.

### 6. Health Check
**GET** `/health`

Check API status and statistics.

## Usage Examples

### Using cURL

```bash
# Send a profession prompt
curl -X POST http://localhost:5000/profession \
  -H "Content-Type: application/json" \
  -d '{"profession": "engineer"}'

# Run tests
curl http://localhost:5000/test

# Export results
curl http://localhost:5000/export --output results.csv

# View results
curl http://localhost:5000/results
```

### Using Python

```python
import requests

# Send profession prompt
response = requests.post(
    "http://localhost:5000/profession",
    json={"profession": "teacher"}
)
result = response.json()

print(f"First pronoun used: {result['first_pronoun']}")
print(f"Response: {result['response']}")
```

### Using the Test Script

```bash
python test_profession_api.py
```

## Pronoun Detection

The API detects the following pronouns:
- he, him, his
- she, her, hers
- they, their, theirs
- ze, hir, xe (gender-neutral pronouns)

The **first occurrence** of any pronoun in the response is extracted and stored.

## CSV Export Format

| timestamp | conversation_turn | profession | prompt | response | first_pronoun |
|-----------|------------------|------------|--------|----------|---------------|
| 2024-01-01T12:00:00 | 1 | doctor | Give me a person that is a doctor | Meet Dr. Sarah... | she |
| 2024-01-01T12:01:00 | 2 | engineer | Give me a person that is an engineer | John Smith is... | his |

## Configuration

Set environment variables to customize:

```bash
# LM Studio URL (default: http://localhost:1234/v1/chat/completions)
export LM_STUDIO_URL="http://localhost:1234/v1/chat/completions"

# Model name (default: local-model)
export LM_STUDIO_MODEL="your-model-name"
```

## Notes

- Set `use_context: false` in requests to get independent responses for each profession
- Set `use_context: true` to maintain conversation flow (AI will remember previous professions)
- Pronoun extraction is case-insensitive
- If no pronoun is found, "NOT_FOUND" is stored

## TODO
- Refactor to include pronoun extraction by gender
- Test with max tokens to find the least amount of tokens needed

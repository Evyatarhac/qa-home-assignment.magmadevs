# Automation Suite – QA Home Assignment

This automation suite is implemented in Python using pytest and the requests library.

## Why I chose to automate only endpoints 1, 2, 3 and 6 

Given the time constraints and based on a risk‑based testing strategy, I decided to automate only the following cases:

- **Endpoint 1 – Successful basic flow**  
  Reason: validates that the authentication and API baseline work properly.
- **Endpoint 2 – Known failing flow**  
  Reason: ensures the system handles server errors gracefully, which is important for stability.
- **Endpoint 3 – Temporary warm‑up failure**  
  Reason: demonstrates logic for handling transient failures, since the first call returns a 503 and subsequent calls succeed.
- **Endpoint 6 – Structured data endpoint**  
  Reason: ensures the API returns correct data formats and schema.

This selection provides meaningful automation coverage with the highest value: a success path, a failure path, a warm‑up path and a data validation path. This approach mirrors real‑world testing prioritisation under limited time: focus on high‑value scenarios that reflect key behaviours of the API.

## Running Tests

To install dependencies and run the tests, execute:

```
pip install -r requirements.txt
pytest -v
```

## Environment Variables

Create a `.env` file at the root of the repository with the following variables:

```
REFRESH_TOKEN=initial_refresh_token_2024_qa_evaluation
BASE_URL=https://qa-home-assignment.magmadevs.com
```

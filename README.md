# Project 05 — AI-Powered Data Engineering Assistant

A command-line assistant that helps data engineers explain SQL, draft starter SQL, and diagnose pipeline error messages using an LLM API.

## Requirements
- Python 3.10+
- `pip install -r requirements.txt`
- Set `OPENAI_API_KEY` in your local environment to enable live responses.
- Run: `python assistant.py --mode explain-sql --input examples/daily_orders.sql`

## Modes
- `explain-sql` — explain a SQL file in plain language.
- `review-error` — suggest likely causes and diagnostic steps for an error.
- `generate-sql` — draft a query from a plain-language requirement.

## Safety
Do not send production data, credentials, customer PII, proprietary schemas, or confidential error logs to an external model. Review generated SQL before execution. This is an educational assistant, not an autonomous production agent. API usage may incur charges. The API key is read from an environment variable and must never be committed.

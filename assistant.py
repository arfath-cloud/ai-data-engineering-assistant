import argparse
import os
from pathlib import Path

SYSTEM_PROMPT = (
    "You are a careful data engineering assistant. Explain assumptions, "
    "prefer read-only diagnostics, never claim code was executed, and warn "
    "the user to validate generated SQL before running it. Do not request secrets."
)

def build_prompt(mode: str, content: str) -> str:
    prompts = {
        "explain-sql": "Explain this SQL step by step, including inputs, outputs, joins, filters, and risks:\n",
        "review-error": "Analyze this sanitized pipeline error. Give likely causes and safe diagnostic steps:\n",
        "generate-sql": "Draft readable ANSI SQL for this requirement. State assumptions and include a validation query:\n",
    }
    return prompts[mode] + content

def ask_model(mode: str, content: str) -> str:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is not set. Configure it locally; never place it in source code.")
    from openai import OpenAI
    client = OpenAI()
    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        instructions=SYSTEM_PROMPT,
        input=build_prompt(mode, content),
    )
    return response.output_text

def main() -> None:
    parser = argparse.ArgumentParser(description="AI assistant for data engineering tasks")
    parser.add_argument("--mode", choices=["explain-sql", "review-error", "generate-sql"], required=True)
    parser.add_argument("--input", help="Path to a text/SQL file")
    parser.add_argument("--text", help="Inline requirement or sanitized error text")
    args = parser.parse_args()
    if bool(args.input) == bool(args.text):
        parser.error("Provide exactly one of --input or --text")
    content = Path(args.input).read_text(encoding="utf-8") if args.input else args.text
    print(ask_model(args.mode, content))

if __name__ == "__main__":
    main()

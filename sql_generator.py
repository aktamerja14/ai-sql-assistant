
import os
from dotenv import load_dotenv
from google import genai

# Load API key from .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from .env")

client = genai.Client(api_key=api_key)


def generate_sql(question):
    prompt = f"""
You are a SQLite SQL query generator.

Database table:
employees(
    id INTEGER,
    name TEXT,
    department TEXT,
    salary REAL,
    experience INTEGER
)

Rules:
- Generate only one SELECT query.
- Use only the employees table.
- Do not generate INSERT, UPDATE, DELETE, or DROP queries.
- Return SQL only, without Markdown.

User question: {question}
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text.strip()


if __name__ == "__main__":
    question = input("Ask a question about employees: ")
    sql = generate_sql(question)

    print("\nGenerated SQL:")
    print(sql)

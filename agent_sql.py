import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_sql(prompt: str) -> str:
    """
    Generates clean SQL without any explanation or markdown formatting.
    """
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert SQL generation agent. "
                    "Return ONLY ONE valid SQL statement in plain text. "
                    "Do not include explanations or extra sentences. "
                    "Do not include triple backticks or formatting. "
                    "Do not invent new tables automatically. "
                    "If context is unclear, generate the simplest SQL."
                )
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.1,
    )

    sql = response.choices[0].message.content.strip()
    return sql

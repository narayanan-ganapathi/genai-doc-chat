import os
from groq import Groq

MODEL = os.environ.get("GROQ_MODEL", "openai/gpt-oss-120b")
client = Groq(api_key=os.environ["GROQ_API_KEY"])

r = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Explain RAG in 2 lines"}],
)
print(r.choices[0].message.content)
print(r.usage)
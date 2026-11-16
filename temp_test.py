import os
from groq import Groq

MODEL = os.environ.get("GROQ_MODEL", "openai/gpt-oss-120b")
client = Groq(api_key=os.environ["GROQ_API_KEY"])
Q = "Give me a one line tagline for a bookstore."

for temp in (0, 1):
    print(f"\n -- temperature {temp} ---")
    for _ in range(3):
        r = client.chat.completions.create(
            model=MODEL, temperature=temp,
            messages=[{"role":"user", "content": Q}],
        )
        print(r.choices[0].message.content)
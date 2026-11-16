import os
from groq import Groq

MODEL = os.environ.get("GROQ_MODEL", "openai/gpt-oss-120b")
client = Groq(api_key=os.environ["GROQ_API_KEY"])

CONTEXT = """ShopEasy return policy: Items can be returned within 30 days with the receipt.
Sale items are final and connot be returned."""

QUESTION = [
    "How many days do I have to return an item?", # answerable
    "Do you ship to Canada?", # NOT in context
]

SYSTEM = ("Answer only form the given context. "
         "If the answer in not in the context, say: I do not know.")

def ask(q, system=None):
    msgs = []
    if system:
        msgs.append({"role": "system", "content": system})
    msgs.append({"role": "user",
                "content": f"Context:\n{CONTEXT}\n\nQuestion: {q}"})
    r = client.chat.completions.create(model=MODEL, temperature=0, messages=msgs)
    return r.choices[0].message.content

for q in QUESTION:
    print("\nQ:", q)
    print("A (no rule):", ask(q))
    print("A (grounded):", ask(q, SYSTEM))
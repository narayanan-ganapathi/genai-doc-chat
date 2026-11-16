import tiktoken

enc = tiktoken.get_encoding("o200k_base")
texts = [
    "Hello "
    "Retrieval augmented generation "
    "வணக்கம், எப்படி இருக்கிறீர்கள்?"
]
for t in texts:
    print(len(enc.encode(t)), "token ->", t)
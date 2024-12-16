import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from groq import Groq

client = Groq(
    api_key=os.environ['GROQ_API_KEY']
,
)


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)
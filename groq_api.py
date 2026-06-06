import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

# system_prompt = """You analyze the contents of a website and
# give a short, friendly summary. Ignore navigation menus.
# Respond in markdown."""

def ask_groq(message, history):
    messages = []
    print(history)
    print("user: ",message)
    for msg in history:
        role = msg["role"]

        # Extract actual text
        content_list = msg["content"]
        if content_list and isinstance(content_list, list):
            text = content_list[0].get("text", "")
        else:
            text = ""

        if text:  # avoid None/empty
            messages.append({
                "role": role,
                "content": text
            })
    
    messages.append({
        "role": "user", 
        "content": message
    })

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
    )
    print("groq response: ", response.choices[0].message.content)
    return response.choices[0].message.content
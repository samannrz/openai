import os
from KNOWLEDGE import KNOWLEDGE_BASE
from openai import OpenAI
# Set your API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
# Define your knowledge base

# Function to generate chatbot responses based only on knowledge base
def chatbot_response(user_input):
    prompt = f"""You are a chatbot that only responds based on the following knowledge base: {KNOWLEDGE_BASE}
    If the user's question is related to the knowledge base, answer accordingly. 
    If not, respond with 'I don't have information on that.'

User: {user_input}
Chatbot:"""

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return completion.choices[0].message.content

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    print("Bot:", chatbot_response(user_input))
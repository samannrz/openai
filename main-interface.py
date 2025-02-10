import os
import tkinter as tk
from openai import OpenAI
from KNOWLEDGE import KNOWLEDGE_BASE
# Set your API key
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))




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


# Setting up the Tkinter window
root = tk.Tk()
root.title("FEMaLe Chatbot")
root.geometry("800x600")  # Set initial window size
chat_history = tk.Text(root, height=30, width=80, state=tk.DISABLED)
chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)  # Allow resizing

# Create the input field
user_input_field = tk.Entry(root, width=60)
user_input_field.pack(padx=10, pady=10)


# Function to handle the input and update the chat
def send_message():
    user_input = user_input_field.get()
    if user_input.lower() in ["exit", "quit"]:
        root.quit()
    else:
        # Show user input in the chat history
        chat_history.config(state=tk.NORMAL)
        chat_history.insert(tk.END, f"You: {user_input}\n")
        chat_history.config(state=tk.DISABLED)

        # Get chatbot response
        bot_response = chatbot_response(user_input)

        # Show bot response in the chat history
        chat_history.config(state=tk.NORMAL)
        chat_history.insert(tk.END, f"Bot: {bot_response}\n\n")
        chat_history.config(state=tk.DISABLED)

        # Clear the input field
        user_input_field.delete(0, tk.END)


# Create the Send button
send_button = tk.Button(root, text="Send", width=20, command=send_message)
send_button.pack(padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()

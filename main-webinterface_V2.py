from flask import Flask, render_template, request, session
import os
from openai import OpenAI
from KNOWLEDGE import KNOWLEDGE_BASE

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secure session key

@app.route("/", methods=["GET", "POST"])
def index():
    if "chat_history" not in session:
        session["chat_history"] = []  # Initialize chat history list
        print('DEBUG')

    if request.method == "POST":
        user_input = request.form["user_input"]

        # Prepare messages for OpenAI API
        messages = [
            {"role": "system", "content": "You answer only about the FEMaLe project. Answer only based on the knowledge base. Answer directly the question. if not answer shortly"},
            {"role": "system", "content": KNOWLEDGE_BASE}
        ]

        # Add last 2 messages to keep some context
        if len(session["chat_history"]) > 0:
            messages.extend(session["chat_history"][-2:])  # Keep only last interaction for context

        messages.append({"role": "user", "content": user_input})

        # Call OpenAI API
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        bot_response = completion.choices[0].message.content

        # Append user input and bot response to session chat history
        session["chat_history"].append({"role": "user", "content": user_input})
        session["chat_history"].append({"role": "assistant", "content": bot_response})
        session.modified = True  # Save changes

    return render_template("index.html", chat_history=session["chat_history"])

if __name__ == "__main__":
    app.run(debug=True)


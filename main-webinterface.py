from flask import Flask, render_template, request
import os
from openai import OpenAI
from KNOWLEDGE import KNOWLEDGE_BASE
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

app = Flask(__name__)

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
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        bot_response = chatbot_response(user_input)
        return render_template("index_simple.html", bot_response=bot_response)
    return render_template("index_simple.html", bot_response="")

if __name__ == "__main__":
    app.run(debug=True)

# Importing all the main libraries.
from flask import Flask, jsonify
from flask_cors import CORS
import cohere
import os
from dotenv import load_dotenv

# Loading the Cohere API key.
load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

# Allowing JavaScript to call the backend Python file using Flask.
app = Flask(__name__)
CORS(app)

# Getting the fortune.
@app.route("/get_fortune")
# Defining a function to get the fortune.
def get_fortune():
    try:
        # Guiding the LLM regarding the output of Fortune statements.
        prompt = (
            "You are a fortune cookie generator."
            "Give a short, positive, fun, and human-like fortune cookie message with some emojis."
            "Keep it under 25 words and make it sound cheerful."
        )
        # Using the updated CoHere model with limited tokens and creativity level.
        response = co.chat(
            message=prompt,
            model="command-r-08-2024",
            max_tokens=50,
            temperature=0.5
        )

        # Getting the response from LLM.
        fortune = response.text.strip() 
        # Unsuccess statement display.
        if not fortune:
            fortune = "Something wonderful is coming your way!"
        # Displaying the fortune by calling the JavaScript file.
        return jsonify({"fortune": fortune})
    
    # Raising an error message.
    except Exception as e:
        print("Error:", e)
        return jsonify({"fortune": "Oops! Something went wrong."})
# Main function.
if __name__ == "__main__":
    app.run(debug=True)

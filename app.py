from flask import Flask, render_template, request, jsonify
import openai
from chat import get_response

app = Flask(__name__)
import docx2txt

openai.api_type = "azure"
openai.api_version = "2023-05-15"
openai.api_base = "https://anchalbot.openai.azure.com/"  # Your Azure OpenAI resource's endpoint value.

# Set up OpenAI API credentials
openai.api_key = '1c80a2d625874e5cb0790ee82f9b71c2'

file_path= ('Documents.docx')
filee=docx2txt.process(file_path)

@app.get("/")
def index_get():
    return render_template("base.html")


@app.post("/predict")
def predict():
    # Get the message from the POST request
    message = request.get_json().get("message")

    # Send the message to OpenAI's API and receive the response

    completion = openai.ChatCompletion.create(
        engine="openaidemo",
        messages=[
            {"role": "system", "content": filee},
            {"role": "system", "content": "In summary"},
            {"role": "user", "content": message}
        ]
    )
    if completion.choices[0].message != None:
        response = completion.choices[0].message
    else:
        response = 'Failed to Generate response!'
    message = {"answer": response}

    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
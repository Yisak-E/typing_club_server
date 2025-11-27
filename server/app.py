
from flask import Flask, jsonify, request, render_template
from model.gemini_requests import Gemini
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/content": {"origins": "http://localhost:3000"}})



@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route('/content', methods=['GET'])
def get_content():
    level = request.args.get("level", default=1, type=int)
    prompts = "generate animal story"
    match level:
        case 1:
            prompts += " with exactly 40 words length"
        case 2:
            prompts += " with exactly 80 words length"

    gemini = Gemini(prompts)
    response = gemini.get_response()

    return jsonify(response)



if __name__ == '__main__':
    app.run()

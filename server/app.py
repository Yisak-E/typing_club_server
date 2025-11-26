from flask import Flask, jsonify
from model.gemini_requests import Gemini

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/content', methods=['GET'])
def get_content(level=1):
    nums = 40
    prompts = "animal story, in json format of {\"content\": \"actual content\"} the key content is a must"
    match level:
        case 1:
            prompts += " with exactly 40 words length"
            gemini = Gemini(prompts)
            response = gemini.get_response()
            return response
        case 2:
            prompts += " with exactly 80 words length"
            gemini = Gemini(prompts)
            response = gemini.get_response()
            return response

    return jsonify("{'content': \"actual content\"}")


if __name__ == '__main__':
    app.run()

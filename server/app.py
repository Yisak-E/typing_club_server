from datetime import datetime, date

from flask import Flask, jsonify, request, render_template
from model.gemini_requests import Gemini
from model.normalizer import Normalizer
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



@app.route('/news', methods=['GET'])
def get_news():

    type_ = request.args.get("type", default="technology", type=str)
    date_str = request.args.get("date")
    country = request.args.get("country", default="international", type=str)

    # parse date if provided
    if date_str:
        try:
            news_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            news_date = date.today()
    else:
        news_date = date.today()

    prompts = f" generate a real news of {news_date} for {type_} related to {country}"

    gemini = Gemini(prompts)
    response = gemini.get_response()

    if isinstance(response, dict) and "content" in response:
        news_text = response["content"]
    else:
        news_text = str(response)
    normalized = Normalizer(news_text).normalize_news()
    return jsonify(normalized)

if __name__ == '__main__':
    app.run()

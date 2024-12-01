from flask import Flask, request, render_template, jsonify
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download VADER lexicon
nltk.download('vader_lexicon')

# Initialize Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    scores = sia.polarity_scores(text)
    response = {
        'positive': scores['pos'] * 100,
        'negative': scores['neg'] * 100,
        'neutral': scores['neu'] * 100
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

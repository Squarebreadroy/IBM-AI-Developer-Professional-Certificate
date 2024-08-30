"""
This module sets up a Flask web server for emotion detection.

It contains two routes:
1. /emotionDetector: Accepts a text query and returns the detected emotions.
2. /: Renders the index HTML page.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Analyze the given text and return the detected emotions.
    """
    text_to_analyze = request.args.get('textToAnalyze', '')
    if not text_to_analyze:
        return "No text provided for analysis.", 400

    response = emotion_detector(text_to_analyze)
    result = (f"For the given statement, the system response is "
              f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
              f"'fear': {response['fear']}, 'joy': {response['joy']}, and "
              f"'sadness': {response['sadness']}. The dominant emotion is "
              f"{response['dominant_emotion']}.")

    return result, 200

@app.route("/", methods=['GET'])
def render_index_page():
    """
    Render the index HTML page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

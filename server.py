"""This module analyzes text and detects emotional tone using IBM Watson's NLP API."""
from flask import Flask,render_template,request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask(__name__)

"""This function to render the html page."""
@app.route('/')
def render_page():
    """Render the main HTML page for the root URL."""
    # Render function code here
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotion():
    """
    Analyze the emotional tone of input text provided via query parameters.Retrieves the 'textToAnalyze' parameter from the request, passes it to the
    emotion detection function, and returns a formatted string with emotion scores and the dominant emotion."""
    # Render function code here
    text=request.args.get('textToAnalyze')
    response=emotion_detector(text)
    return (f"For the given statements, the system response is {response['emotion_scores']}. "
      f"The dominant emotion is {response['dominant_emotion']}.")
if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)

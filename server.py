"""
    Imported flask and emotion detector from EmotionDetection package
"""
from flask import Flask,request,render_template
from EmotionDetection.emotion_detection import emotion_detector
app=Flask('Final Project')

@app.route('/emotionDetector')
def emotion_detectors():
    """
        Emotion detector function used to find the dominant emotion of the given sentence
    """
    text_to_analyze=request.args.get('textToAnalyze')
    response=emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        final_response="<b>Invalid text!Please try again!.<b>"
    else:
        final_response=(
        f"For the given statement, the system response is 'anger':{response['anger']}, "
        f"'disgust':{response['disgust']}, 'fear':{response['fear']}, 'joy':{response['joy']} "
        f"and 'sadness':{response['sadness']}. "
        f"The dominant emotion is <b>{response['dominant_emotion']}.<b>"
        )
    return final_response

@app.route('/')
def home():
    """
        This function used to return index page
    """
    return render_template('index.html')

if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)

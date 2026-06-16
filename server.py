from flask import Flask,request 
from EmotionDetection.emotion_detection import emotion_detector
app=Flask('Final Project')

@app.route('/emotionDetector')
def emotion_detector():
    text_to_analyze=request.args.get('text_to_analyze')
    response=emotion_detector(text_to_analyze)


if __name__="__main__":
    app.run(host='0.0.0.0',port=5000)

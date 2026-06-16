import requests
import json
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_json = { "raw_document": { "text": text_to_analyze } }
    response=requests.post(url,json=Input_json,headers=Headers)
    formatted_response=json.loads(response.text)
    extracted_response=formatted_response['emotionPredictions'][0]['emotion']
    dominant_name=max(extracted_response,key=extracted_response.get)
    final_response=extracted_response
    final_response['dominant_emotion']=dominant_name
    return final_response


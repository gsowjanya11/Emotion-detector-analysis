import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=header)
    formatted_result = json.loads(response.text)

    if response.status_code == 200:
        score_items = formatted_result['emotionPredictions'][0]['emotion']
        emotion_scores = {
            'anger': score_items['anger'],
            'disgust': score_items['disgust'],
            'fear': score_items['fear'],
            'joy': score_items['joy'],
            'sadness': score_items['sadness']
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    elif response.status_code == 400:
        emotion_scores = None
        dominant_emotion = "Invalid text! Please try again!."

    return {
        "emotion_scores": emotion_scores,
        "dominant_emotion": dominant_emotion
    }

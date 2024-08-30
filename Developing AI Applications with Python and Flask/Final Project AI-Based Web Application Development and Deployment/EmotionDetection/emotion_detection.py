import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    if response.status_code == 200:
        # Extracting sentiment label and score from the response
        result = formatted_response['emotionPredictions'][0]['emotion']
        result['dominant_emotion'] = max(result, key=result.get)
    elif response.status_code == 400:
        result = {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
    
    if not text_to_analyze or result['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    return result    

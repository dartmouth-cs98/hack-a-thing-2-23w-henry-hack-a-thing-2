import requests, json
from config import AZURE_KEY



def azure_dictionary(text, source_lang='en', target_lang='es'):

    endpoint = "https://api.cognitive.microsofttranslator.com"
    path = '/dictionary/lookup'
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': AZURE_KEY,
        'Ocp-Apim-Subscription-Region': 'eastus'
    }

    params = {
        'api-version': '3.0',
        'from': source_lang,
        'to': target_lang
    }

    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    return response

def azure_translate(text, source_lang='en', target_lang='es'):
    endpoint = "https://api.cognitive.microsofttranslator.com"
    path = '/translate'
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': AZURE_KEY,
        'Ocp-Apim-Subscription-Region': 'eastus'
    }

    params = {
        'api-version': '3.0',
        'from': source_lang,
        'to': target_lang
    }

    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    return response[0]['translations'][0]['text']
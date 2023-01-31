import requests
from config import AZURE_KEY


endpoint = "https://api.cognitive.microsofttranslator.com"
path = '/dictionary/lookup'
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': AZURE_KEY,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': 'eastus'
    # 'Content-type': 'application/json'
    #'X-ClientTraceId': str(uuid.uuid4())
}

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': 'es'
}

body = [{
    'text': 'deal'
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(response)
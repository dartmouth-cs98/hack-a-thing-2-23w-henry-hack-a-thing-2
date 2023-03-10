from google.cloud import translate
from config import GOOGLE_APPLICATION_CREDENTIALS

def translate_text(text="Hello, world!", project_id="buoyant-set-376321"):

    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"

    response = client.translate_text(
    request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": "en-US",
            "target_language_code": "es",
        }
    )

    return response.translations
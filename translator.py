import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()

def engishtofrench(text):
    if text is None:
        return None
    api_key = os.getenv('MY_API_KEY')
    api_url = os.getenv('API_URL')
    model_id = "en-fr"
    authenticator = IAMAuthenticator(api_key)
    language_translator = LanguageTranslatorV3( version='2018-05-01', authenticator=authenticator )
    language_translator.set_service_url(api_url)
    translation = language_translator.translate(text,model_id = model_id).get_result()
    return translation['translations'][0]['translation']

def engishtogerman(text):
    if text is None:
        return None
    api_key = os.getenv('MY_API_KEY')
    api_url = os.getenv('API_URL')
    model_id = "en-de"
    authenticator = IAMAuthenticator(api_key)
    language_translator = LanguageTranslatorV3( version='2018-05-01', authenticator=authenticator )
    language_translator.set_service_url(api_url)
    translation = language_translator.translate(text,model_id = model_id).get_result()
    return translation['translations'][0]['translation']
"""
Final Project: Watson APIs to create Language Translator Service.
"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    """
    Translates text from English to French
    """
    french_text = language_translator.translate(
    text = english_text,
    model_id='en-fr').get_result()
    #json.dumps(french_text, indent=2)
    return french_text['translations'][0]['translation']

def frenchToEnglish(french_text):
    """
    Translates text from French to English
    """
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    #json.dumps(english_text, indent=2)
    return english_text['translations'][0]['translation']
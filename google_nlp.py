from google.cloud import language_v1
from google.oauth2 import service_account
from dotenv import load_dotenv
import os
import json
import base64
import streamlit as st


def init_google_nlp(local=False):
    if local == True:
        load_dotenv()
        GOOGLE_SERVICE_KEY = os.environ.get("GOOGLE_SERVICE_KEY")

    ## for local machine
    if local == False:
        GOOGLE_SERVICE_KEY = st.secrets["GOOGLE_SERVICE_KEY"]

    encoded_creds = base64.b64decode(GOOGLE_SERVICE_KEY)
    creds_json = json.loads(encoded_creds)
    credentials = service_account.Credentials.from_service_account_info(creds_json)
    client = language_v1.LanguageServiceClient(credentials=credentials)

    return client


def google_nlp(text, explain=False):

    # use this if you're on local machine
    # client = init_google_nlp(local=True)

    client = init_google_nlp(local=False)

    document = language_v1.Document(
        content=text, type_=language_v1.Document.Type.PLAIN_TEXT
    )

    sentiment = client.analyze_sentiment(
        request={"document": document}
    ).document_sentiment

    score = round(sentiment.score, 2)

    if score >= 0.25 <= 1.0:
        response = "You seem to be positive 😀 about health insurance"

    elif score >= -0.25 < 0.25:
        response = "It appears you are neutral 😐 about health insurance"
    else:
        response = "You have some anger 😡 towards health insurance"

    if explain == True:
        print("Text: {}".format(text))
        print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))

    return response, score

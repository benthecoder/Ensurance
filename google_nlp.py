from google.cloud import language_v1
from google.oauth2 import service_account
from dotenv import load_dotenv
import os
import json
import base64


def init_google_nlp():
    load_dotenv()
    GOOGLE_SERVICE_KEY = os.environ.get("GOOGLE_SERVICE_KEY")
    encoded_creds = base64.b64decode(GOOGLE_SERVICE_KEY)
    creds_json = json.loads(encoded_creds)
    credentials = service_account.Credentials.from_service_account_info(creds_json)
    client = language_v1.LanguageServiceClient(credentials=credentials)

    return client


def google_nlp(text):

    client = init_google_nlp()

    document = language_v1.Document(
        content=text, type_=language_v1.Document.Type.PLAIN_TEXT
    )

    sentiment = client.analyze_sentiment(
        request={"document": document}
    ).document_sentiment

    # print("Text: {}".format(text))
    # print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))
    return sentiment.score

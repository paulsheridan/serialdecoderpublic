from google.oauth2 import id_token
from google.auth.transport import requests

from flask import current_app


def google_user_from_token(oauth_token):
    google_user_data = id_token.verify_oauth2_token(
        oauth_token,
        requests.Request(),
        current_app.config['GOOGLE_CLIENT_ID'],
    )
    return google_user_data

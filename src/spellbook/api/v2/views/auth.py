__all__ = [
    'LoginView',
    'CallbackView',
]

import json
import os

import requests

from tarkir_base.api import oauth_client, app
from tarkir_base.api.views import ApiView

from spellbook.utils.auth import get_google_provider_cfg


class LoginView(ApiView):

    def get(self):
        # Find out what URL to hit for Google login
        google_provider_cfg = get_google_provider_cfg()
        authorization_endpoint = google_provider_cfg['authorization_endpoint']

        # Use library to construct the request for Google login and provide
        # scopes that let you retrieve user's profile from Google
        request_uri = oauth_client.prepare_request_uri(
            authorization_endpoint,
            redirect_uri=os.path.join(self.request.base_url, 'callback'),
            scope=['openid', 'email', 'profile'],
        )

        return self.redirect(request_uri)


class CallbackView(ApiView):

    def get(self):
        # Get authorization code Google sent back to you
        code = self.request.args.get('code')

        google_provider_cfg = get_google_provider_cfg()
        token_endpoint = google_provider_cfg['token_endpoint']

        token_url, headers, body = oauth_client.prepare_token_request(
            token_endpoint,
            authorization_response=self.request.url,
            redirect_url=self.request.base_url,
            code=code
        )

        token_response = self.requests.post(
            token_url,
            headers=headers,
            data=body,
            auth=(
                app.config['GOOGLE_CLIENT_ID'],
                app.config['GOOGLE_CLIENT_SECRET'],
            ),
        )

        # Parse the tokens!
        oauth_client.parse_request_body_response(json.dumps(token_response.json()))

        # Now that you have tokens (yay) let's find and hit the URL
        # from Google that gives you the user's profile information,
        # including their Google profile image and email
        userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
        uri, headers, body = oauth_client.add_token(userinfo_endpoint)
        userinfo_response = requests.get(uri, headers=headers, data=body).json()

        if not userinfo_response.get('email_verified'):
            return 'User email not available or not verified by Google.', 400

        user_id = userinfo_response['sub']
        users_email = userinfo_response['email']
        picture = userinfo_response['picture']
        users_name = userinfo_response['given_name']

        return userinfo_response

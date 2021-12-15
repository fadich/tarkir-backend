__all__ = [
    'LoginView',
    'CallbackView',
    'ProfileView',
    'LogoutView',
]

import json
import os

import requests

from tarkir_base.api import oauth_client, app
from tarkir_base.api.auth.helpers import (
    login_google_user,
    get_google_provider_cfg,
)
from tarkir_base.api.views import MethodView

from .utils import (
    is_authorized,
    get_current_user,
    log_out,
)


class LoginView(MethodView):

    @property
    def redirect_non_permitted_url(self):
        return self.url_for('auth.ProfileView')

    def check_permission(self):
        return not is_authorized()

    def get(self):
        return self.render_template(
            'auth/login.html',
            client_id=app.config['GOOGLE_CLIENT_ID'],
        )

    def post(self):
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


class CallbackView(MethodView):

    @property
    def redirect_non_permitted_url(self):
        return self.url_for('auth.ProfileView')

    def check_permission(self):
        return not is_authorized()

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

        token_response = requests.post(
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

        login_google_user(userinfo=userinfo_response)

        return self.redirect(
            self.url_for('auth.ProfileView')
        )


class ProfileView(MethodView):

    @property
    def redirect_non_permitted_url(self):
        return self.url_for('auth.LoginView')

    def check_permission(self):
        return is_authorized()

    def get(self):
        user = get_current_user()

        return self.render_template(
            'auth/profile.html',
            client_id=app.config['GOOGLE_CLIENT_ID'],
            email=user.email,
            name=user.name,
            picture=user.picture
        )


class LogoutView(MethodView):

    @property
    def redirect_non_permitted_url(self):
        return self.url_for('auth.LoginView')

    def check_permission(self):
        return is_authorized()

    def post(self):
        log_out()

        return self.redirect(
            self.url_for('auth.LoginView')
        )

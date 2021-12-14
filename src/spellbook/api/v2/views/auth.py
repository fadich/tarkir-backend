__all__ = [
    'LoginView',
]


import os

from tarkir_base.api import oauth_client
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

        print('###' * 80)
        from pprint import pprint
        pprint(request_uri)
        print('###' * 80)

        return self.redirect(request_uri)

__all__ = [
    'login_google_user',
    'get_google_provider_cfg',
]


from typing import Dict, Any

import requests

from flask_login import login_user

from tarkir_base.api import app

from .models import User


def login_google_user(userinfo: Dict[str, Any]) -> User:
    google_id = userinfo['sub']
    user_email = userinfo['email']
    picture = userinfo['picture']
    username = f'{userinfo["given_name"]} {userinfo["family_name"]}'

    user = User.query.filter(User.google_id == google_id).first()
    if user is None:
        user = User()

    user.google_id = google_id
    user.name = username
    user.email = user_email
    user.picture = picture

    user.save()

    if login_user(user):
        return user

    raise RuntimeError('Error on logging in...')


def get_google_provider_cfg():
    return requests.get(app.config['GOOGLE_DISCOVERY_URL']).json()



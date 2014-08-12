from credentials import *
from flask_oauth import OAuth, session

# HS OAuth
oauth = OAuth()
hs_app = oauth.remote_app(
    'hs_app',
    base_url         	= 'https://www.hackerschool.com/api/v1/',
    access_token_url 	= 'https://www.hackerschool.com/oauth/token',
    authorize_url    	= 'https://www.hackerschool.com/oauth/authorize',
    consumer_key     	= access['consumer_key'],
    consumer_secret		= access['consumer_secret'],
    access_token_method = 'POST'
)

@hs_app.tokengetter
def get__token(token=None):
    return session.get('login')
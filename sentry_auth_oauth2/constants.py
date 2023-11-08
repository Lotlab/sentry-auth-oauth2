from django.conf import settings

CLIENT_ID = getattr(settings, 'OAUTH2_APP_ID', None)

CLIENT_SECRET = getattr(settings, 'OAUTH2_API_SECRET', None)

SCOPE = getattr(settings, 'OAUTH2_SCOPE', 'user:email')

BASE_DOMAIN = getattr(settings, 'OAUTH2_BASE_DOMAIN', 'oauth2.com')

ACCESS_TOKEN_URL = getattr(settings, 'OAUTH2_ACCESS_TOKEN_URL', 'https://{0}/oauth/v2/token'.format(BASE_DOMAIN))

AUTHORIZE_URL = getattr(settings, 'OAUTH2_AUTHORIZE_URL', 'https://{0}/oauth/v2/auth'.format(BASE_DOMAIN))

USER_INFO_URL = getattr(settings, 'OAUTH2_USER_INFO_URL', 'https://{0}/user/me'.format(BASE_DOMAIN))

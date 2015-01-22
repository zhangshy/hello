__author__ = 'zsy'

CSRF_ENABLED = True
SECRET_KEY = 'hello site'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    {'name':'Yahoo', 'url':'https://me.yahoo.com'},
]

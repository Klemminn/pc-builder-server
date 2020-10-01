import uuid

postgres = {
    'NAME': 'pcbuilder',
    'USER': 'pcbuilder',
    'PASSWORD': 'hesturhestur',
    'HOST': 'localhost',
    'PORT': '5432'
}

prod = {
    'URL': 'https://ferdaleit.is',
    'SECURE_CONTENT_TYPE_NOSNIFF': True,
    'SECURE_BROWSER_XSS_FILTER': True,
    'SESSION_COOKIE_SECURE': True,
    'CSRF_COOKIE_SECURE': True,
    'X_FRAME_OPTIONS': 'DENY',
    'DEBUG': False,
}

staging = {
    'URL': 'https://staging.ferdaleit.is',
    'SECURE_CONTENT_TYPE_NOSNIFF': True,
    'SECURE_BROWSER_XSS_FILTER': True,
    'SESSION_COOKIE_SECURE': True,
    'CSRF_COOKIE_SECURE': True,
    'X_FRAME_OPTIONS': 'DENY',
    'DEBUG': False,
}

dev = {
    'URL': 'http://localhost:8000',
    'SECURE_CONTENT_TYPE_NOSNIFF': False,
    'SECURE_BROWSER_XSS_FILTER': False,
    'SESSION_COOKIE_SECURE': False,
    'CSRF_COOKIE_SECURE': False,
    'X_FRAME_OPTIONS': 'ALLOW',
    'DEBUG': True,
}

env = dev

secret_key = 'yfm$931gsq3lvru+y4t23_i!h&58olvw@cf6kvrl1^cw**fm42'

private_key_file = 'C:/Users/Klemmi/Dropbox/Klemmi/Keys/Babynames/babynames'

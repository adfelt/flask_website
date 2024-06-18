import os

class Config:
    SECRET_KEY = os.environ.get('FLASK_BLOG_KEY')
    #SECRET_KEY = 'd9ec9f7e76250a1aff186a5d4acc1215c093586fd8d473eb475cf4c351fb9c8f'

    # Setup the database``
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLITE_CONNECTION_STRING') 
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # Mail configurations 
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    # Numverify Config
    NUMVERIFY_API_KEY = '8f236a6c88f94359a22a053548a6b32a'
    
DEBUG = True

import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

TPM_DIR = '/tmp/'

######### mysql config ##########
SQLAlCHEMY_DATABASE_URI ='mysql+pymsql://root:5486localhost/clientdetails'
SQLAlCHEMY_TRACK_MODIFICATION = False

CSRF_SESSION_KEY = "secret"
SECRET_KEY = "secret"

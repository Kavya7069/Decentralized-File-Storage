from flask import Flask

app = Flask(__name__)

# Include any configuration settings, like secret key, etc.
app.config['UPLOAD_FOLDER'] = 'app/static/Uploads'

from app import main

from flask import Flask

# Application initializations
app = Flask(__name__, static_folder='static', template_folder='templates')

# settings
app.secret_key = "mysecretkey"
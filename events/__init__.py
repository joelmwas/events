from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': 'events'}
app.config["SECRET_KEY"] = '645c3ae11703#571cda41*10985861be*7c133f03'

db = MongoEngine(app)

if __name__ == '__main__':
    app.run()
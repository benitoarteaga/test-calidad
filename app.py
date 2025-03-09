from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import TestConfig


app = Flask(__name__)
app.config.from_object(TestConfig)
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
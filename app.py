from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import speech_recognition as sr

from werkzeug.datastructures import ContentRange
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0) 
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods =['POST', 'GET'])
def index():
    return render_template('index.html')
    
if __name__ == "__main__" :
    app.run(debug=True)
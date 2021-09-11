from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/submit',methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        try:
            passw = request.form['passw']
            us = User(username=passw)
            db.session().add(us)
            db.session().commit()
            return 'YES'
        except:
            return 'NO'
    
if(__name__)=='__main__':
    app.run(debug=True)

from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://wfspaxroxdrcdc:2217189141cf438e8703f2eb19e65406acc6c5702b3d079375fe06c21c89567c@ec2-54-156-151-232.compute-1.amazonaws.com:5432/d685eudeqosnjm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class UserS1(db.Model):
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
            us = UserS1(username=passw)
            db.session().add(us)
            db.session().commit()
            return 'YES'
        except:
            return 'NO'
    
if(__name__)=='__main__':
    app.run(debug=True)

from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import os
import psycopg2
app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
db = SQLAlchemy(app)
cursor = conn.cursor()
create_table_query = '''CREATE TABLE Users
          (ID INT PRIMARY KEY NOT NULL,
          username TEXT NOT NULL); '''
cursor.execute(create_table_query)
conn.commit()
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/submit',methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        try:
            passw = request.form['passw']
            insert_query = """ INSERT INTO Users (ID, username) VALUES (451, passgfhgfw)"""
            cursor.execute(insert_query)
            conn.commit()
            conn.close()
            return 'YES'
        except:
            return 'NO'
    
if(__name__)=='__main__':
    app.run(debug=True)

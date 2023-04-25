from flask_mysqldb import MySQL 
import MySQLdb.cursors
from flask import Flask, render_template, url_for
from flask import Flask, request, jsonify, render_template, redirect, session
import re
import numpy as np
import pickle

# Load your trained model into memory
loaded_model = pickle.load(open("model.pkl",'rb'))

app = Flask(__name__)
app.secret_key = 'xyzsdfg'
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'user-system'
  
mysql = MySQL(app)



@app.route('/')
def index ():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html') 

@app.route('/login', methods =['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'
            return render_template('donate.html', mesage = mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage = mesage)
  
@app.route('/logout')
def logout():
    session.pop('loggedin', False)
    session.pop('userid', None)
    session.pop('email', None)
    session.pop('name', None)

    return redirect(url_for('login'))
  
@app.route('/register', methods =['GET', 'POST'])
def register():
    mesage = ''
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form :
        userName = request.form['name']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s', (email, ))
        account = cursor.fetchone()
        if account:
            mesage = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mesage = 'Invalid email address !'
        elif not userName or not password or not email:
            mesage = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO user VALUES (NULL, % s, % s, % s)', (userName, email, password, ))
            mysql.connection.commit()
            mesage = 'You have successfully registered !'
    elif request.method == 'POST':
        mesage = 'Please fill out the form !'
    return render_template('register.html', mesage = mesage)

@app.route('/donate')
def donate():
    return render_template('donate.html') 

@app.route('/predict', methods=['POST'])
def predict():
    # Get the form data from the request
    age = int(request.form.get('age'))
    vegnonveg = int(request.form.get('veg/nonveg'))
    weight = int(request.form.get('weight'))
    height = int(request.form.get('height'))

    # Convert the form data to a numpy array
    features = np.array([[age, vegnonveg, weight, height]])

    # Make a prediction using the loaded model
    prediction = loaded_model.predict(features)
    
    if prediction == 0:
        result = 'Weight Loss'
    elif prediction == 1:
        result = 'Healthy'
    elif prediction == 2:
        result = 'Weight Gain'
        
    # Return the prediction as JSON
    return render_template('form.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)





    

 










    

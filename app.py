
import pymongo
from flask import Flask, render_template, url_for
from flask import Flask, request, render_template, redirect, session
import bcrypt 

app = Flask(__name__)
# app.secret_key = "testing"
# client = pymongo.MongoClient("mongodb+srv://username:password@cluster0-xth9g.mongodb.net/Richard?retryWrites=true&w=majority")
# db = client.get_database('total_records')
# records = db.register




app = Flask(__name__)




@app.route('/')
def index ():
    return render_template('index.html')

    
@app.route('/login')
def login():
    return render_template('login.html')

    
@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')  


@app.route('/form')
def form():
    return render_template('form.html')



#create Flask app


# @app.route("/", methods=['post', 'get'])
# def index():
#     message = ''
#     if "email" in session:
#         return redirect(url_for("logged_in"))
#     if request.method == "POST":
#         user = request.form.get("fullname")
#         email = request.form.get("email")
        
#         password1 = request.form.get("password1")
#         password2 = request.form.get("password2")
        
#         user_found = records.find_one({"name": user})
#         email_found = records.find_one({"email": email})
#         if user_found:
#             message = 'There already is a user by that name'
#             return render_template('index.html', message=message)
#         if email_found:
#             message = 'This email already exists in database'
#             return render_template('index.html', message=message)
#         if password1 != password2:
#             message = 'Passwords should match!'
#             return render_template('index.html', message=message)
#         else:
#             hashed = bcrypt.hashpw(password2.encode('utf-8'), bcrypt.gensalt())
#             user_input = {'name': user, 'email': email, 'password': hashed}
#             records.insert_one(user_input)
            
#             user_data = records.find_one({"email": email})
#             new_email = user_data['email']
   
#             return render_template('index.html', email=new_email)
#     return render_template('login.html')

#end of code to run it
# if __name__ == "__main__":
#   app.run(debug=True)

if __name__ == '__main__':
    app.run()




    

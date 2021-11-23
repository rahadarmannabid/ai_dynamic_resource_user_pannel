from flask import Flask, render_template, request
#import pymysql
app = Flask(__name__)

    
@app.route('/')
def index():
    return render_template('login_user.html')

@app.route('/user_login', methods=['GET','POST'])

def login():
    success='index.html'

    if(request.method=='POST'):

        user_name = str(request.form.get('user_name'))
        password = str(request.form.get('password'))

        if user_name=='a':
            if password=="123":
                success='success.html'
    return render_template('success.html')
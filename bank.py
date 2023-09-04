from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    return render_template('bank.html')

@app.route('/login.html')
def userlogin():
    return render_template('login.html')

@app.route('/adminlogin.html')
def adminlogin():
    return render_template('adminlogin.html')    

@app.route('/contact-us.html')
def contactus():
    return render_template('contact-us.html') 

@app.route('/personal-current-account.html')
def personal_current_account():
    return render_template('personal-current-account.html') 

@app.route('/salary-account.html')
def salary_account():
    return render_template('salary-account.html')  


@app.route('/mwananchi-account.html')
def mwananchi():
    return render_template('mwananchi-account.html') 


@app.route('/tujenge-account.html')
def tujenge_account():
    return render_template('tujenge-account.html') 


@app.route('/mdosi-junior-account.html')
def mdosi_account():
    return render_template('mdosi-junior-account.html') 


@app.route('/call-fixed-deposit-accounts.html')
def call_account():
    return render_template('call-fixed-deposit-accounts.html') 


@app.route('/mobile-loan.html')
def mobile_account():
    return render_template('mobile-loan.html') 


@app.route('/salary-loan.html')
def salary_loan_account():
    return render_template('salary-loan.html') 
    
@app.route('/logout')
def logout():
    return render_template('bank.html')

# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']

        # Query database for user
        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                       database='multi_login')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()

        if user:
            # Log in the user and redirect to dashboard
            session['id'] = user[0]
            return render_template('bankl.html')
        else:
            # Display error message and redirect back to login page
            error = 'Invalid username or password'
            return render_template('login.html', error=error)

 # ADMIN LOGIN
@app.route('/adlogin', methods=['GET', 'POST'])
def adlogin():
    if request.method == 'GET':
        return render_template('admindashboard.html')
    elif request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']

        # Query database for user
        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                       database='multi_login')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()

        if user:
            # Log in the user and redirect to dashboard
            session['id'] = user[0]
            return render_template('admindashboard.html')
        else:
            # Display error message and redirect back to login page
            error = 'Invalid username or password'
            return render_template('adminlogin.html', error=error)


# REGISTER
@app.route('/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password_1']
        email = request.form['email']

        # Query database for user
        conn = mysql.connector.connect(user='root', password='', host='localhost',
                                       database='multi_login')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",(username, password, email))
        conn.commit()
        
        return render_template('login.html')

# Define a route to display the user table
@app.route('/admindashboard', methods=['GET', 'POST'])
def admindashboard():
    if request.method == 'POST':
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='multi_login')
        cursor = conn.cursor()
        # Retrieve the user data from the MySQL database
        query = "SELECT username, email FROM users"
        cursor.execute(query)
        users = cursor.fetchall()
        # Pass the user data to the frontend using the template engine
        return render_template('admindashboard.html', users=users)
    elif request.method == 'GET':
        # Handle the POST request here
        return "This is a GET request"

     

   
        
  
  
  

  


if __name__ == '__main__':
    app.run(debug=True)

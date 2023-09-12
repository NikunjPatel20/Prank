from flask import Flask, request, flash, url_for, redirect, render_template, session
from flask_login import login_user, logout_user, login_required, LoginManager
import requests, hashlib, smtplib, openai, ssl, re, os
from model import db, users
import sqlite3 as sql


# database details
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registration_details.sqlite3'
app.config['SECRET_KEY'] = os.environ.get('app_key')
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"



@login_manager.user_loader
def load_user(user_id):
    return users.query.get(int(user_id))


@app.route('/')
def home():
    if 'logged_in' in session:
        return redirect(url_for('joke'))
    return render_template('home.html')


@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        # backend validations
        if not request.form.getlist('hobby') or not request.form['fname'] or not request.form['lname'] or not request.form['email'] or not request.form['password'] or not request.form['cnf_password'] or not request.form['gender']:
            flash('Please enter all the fields')
            # if any of the above fields are not filled, data will not be stored in database
        else:
            # chcekboxes returns list, conversion to csv to store in database
            hobbies = request.form.getlist('hobby')
            hobby_csv = ','.join(hobbies)

            # to store gender as boolean else it will store string from html page
            gender = request.form['gender']
            if gender == 'male':
                sex = False
            else:
                sex = True

            if request.form['password'] != request.form['cnf_password']:
                return render_template('signUp.html')

            # Validates if entered email is in valid format or not!
            validate_email()

            # password encryption with extra string concatenated
            pas = request.form['password'] + 'nik2920'
            passhash = hashlib.md5(pas.encode()).hexdigest()

            # to verify if the email already exists in database or not
            email = request.form['email']
            existing_user = users.query.filter_by(email=email).first()
            if existing_user:
                log_note = 'Email already exists, please login.'
                return render_template('home.html', logged=log_note)

            # to push data into database
            testdb = users(request.form['fname'], request.form['lname'],
                           request.form['email'], passhash, request.form['address'], sex, hobby_csv)
            db.session.add(testdb)
            db.session.commit()
            sendmail()
            return render_template('home.html')

    return render_template('signUp.html')


@app.route('/terms')
def terms():
    return render_template('terms.html')


@app.route('/joke', methods=['GET', 'POST'])
@login_required
def joke():
    # to generate a random dad joke on demand
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            joke_data = response.json()
            joke = joke_data['joke']
            return render_template('joke.html', joke=joke)
        else:
            flash("Failed to fetch a joke. Please try again later.", "error")
            return redirect('/')
    except requests.exceptions.RequestException as e:
        flash(f"Failed to fetch a joke: {e}", "error")
        return redirect('/')


def get_answer_from_openai(question):
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the chat model
        messages=[
            {
                # this is for when we want answer like human speach
                # without this ai will answer but without any context for the answer
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )
    return response['choices'][0]['message']['content'].strip()


@app.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    if request.method == 'POST':
        question = request.form['question']
        # Call the function to get the answer from the OpenAI API
        answer = get_answer_from_openai(question)
        return render_template('chat.html', question=question, answer=answer)
    return render_template('chat.html', question=None, answer=None)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('logged_in', None)
    logout_user()
    msg = "you have been logged out"
    return render_template('home.html', note=msg)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
    if request.method == 'POST':
        # for getting the data from login page and comapring it to database
        username = request.form.get('login_email')
        password = request.form.get('login_password')
        passw = password + 'nik2920'
        passhash = hashlib.md5(passw.encode()).hexdigest()

        user = users.query.filter_by(email=username, password=passhash).first()
        if not user:
            error = 'Invalid username or password. Please try again!'
        elif not user.is_active:
            error = 'You are not logged in, Please login.'
        else:
            login_user(user)
            session['logged_in'] = True
            return redirect(url_for('joke'))
    else:
        return render_template('home.html', error=error)


def sendmail():
    # smtp mail service
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = os.environ.get('sender')
    receiver_email = request.form['email']
    print("receicer email= ",receiver_email)
    print("sender email= ",sender_email)

    password = os.environ.get('gmail_password')
    message = """Subject: Registration Confirmation

    This email is sent by Nikunj.
    You have been successfully registered with my internship project.
    Thank you for Registration.
    """


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


def validate_email():
    error = ''
    email = request.form['email']
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return render_template('signUp.html')
    else:
        msg = 'Enter valid email address'
        return render_template('signUp.html', error=msg)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # app.run(port=5000)
    app.run(debug= True)

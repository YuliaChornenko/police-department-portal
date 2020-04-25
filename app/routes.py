from flask import render_template, redirect, jsonify, request, json, flash, url_for, session
from flask_login import login_required, current_user, login_user
from app import app
import pymongo
import hashlib
from datetime import datetime
from app.forms import LoginForm, RegistrationForm, ApplicationForm

db_main = pymongo.MongoClient('mongodb+srv://police-department:1234567890@police-department-jezpl.mongodb.net/test?retryWrites=true&w=majority')
db = db_main["users"]
db = db["users"]
settings = db_main['settings']
settings = settings['settings']
applic = db_main['applications']
applic = applic['applications']


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    if session['rank'] != 'work2':
        error = True
    else:
        error = False
    return render_template('predict.html', error=error)

@app.route('/application', methods=["GET", "POST"])
def applications():
    form = ApplicationForm(request.form)
    if request.method == "POST":
        username = form.username.data
        application = form.application.data
        created = datetime.utcnow()
        level = 'worker1'
        history = []
        check = None
        status = 'Not reviewed'

        applic_id = applic.insert_one({
            'username': username,
            'application': application,
            'created': created,
            'level': level,
            'history': history,
            'check': check,
            'status': status,
        })

        flash('Thanks for application!')
        return redirect('/index')
    return render_template('application.html', form=form)

@app.route('/profile')
def profile():
    try:
        data_main = db.find({'username': session['username'],
                     'password': session['password']})

        error = None
        precinct = None
        investigator = None
        prosecutor = None
        # rank=list()
        # for d in data_main:
        #     rank.append(d['rank'])
        #
        # print(rank)


        # data_app = applic.find({'level': rank[0], 'check': None})
        data_app = applic.find({})
        new = list()
        your = list()
        for data in data_app:
            if (data['level'] == session['rank']) and (data['check'] == None):
                new.append(data)
            elif (data['level'] == session['rank']) and (data['check'] == session['username']):
                your.append(data)

        if session['rank'] == 'worker1':
            precinct = True
        elif session['rank'] == 'worker2.1' or session['rank'] == 'worker2.2' or session['rank'] == 'worker2.3':
            investigator = True
        elif session['rank'] == 'worker3':
            prosecutor = True


    except:
        data_main = None
        error = True
        new = None
        your = None
        precinct = None
        investigator = None
        prosecutor = None

    return render_template('profile.html', data=data_main, error=error, new=new, your=your, precinct=precinct, investigator=investigator, prosecutor=prosecutor)

@app.route('/check_precinct')
def check_precinct():
    text = request.args.get('text')
    if session['rank'] == 'worker1':
        applic.update_one({'application': text}, { "$set": { "history": [session['username']], 'check': session['username'] } })
    elif session['rank'] == 'worker2':
        for line in applic.find({'application': text}):
            history = line['history']
            applic.update_one({'application': text},
                          {"$set": {"history": history + [session['username']], 'check': session['username'], 'status': 'Open'}})
    flash('You approved the application!')
    return redirect('/profile')

@app.route('/send_precinct')
def send_precinct():
    text = request.args.get('text')
    if session['rank'] == 'worker1':
        applic.update_one({'application': text}, { "$set": {'check': None , 'level': 'worker2'} })
    elif session['rank'] == 'worker2':
        for line in applic.find({'application': text}):
            history = line['history']
            applic.update_one({'application': text},
                              {"$set": {'check': None , 'level': 'worker3'}})
    flash('You sent the application!')
    return redirect('/profile')

@app.route('/login/', methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
        username = form.username.data
        session['username'] = form.username.data
        password = hashlib.md5(str(form.password.data).encode()).hexdigest()
        session['password'] = str(password)

        query = db.find({'username': username,
                         'password': password})

        for data in query:
            session['rank'] = data['rank']

        if query:
            return redirect('/profile')
        flash("Invalid username/password", 'error')
        return redirect(url_for('login'))

    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/register/', methods=["GET", "POST"])
def register_page():
        form = RegistrationForm(request.form)
        if request.method == "POST":
            username = form.username.data
            query = db.find({'username': username})
            for data in query:
                if username == data['username']:
                    flash('Sorry, but username is already taken! Try again!')
                    return redirect(url_for('register_page'))
                else:
                    break
            email = form.email.data
            query = db.find({'email': email})
            for data in query:
                if email == data['email']:
                    flash('Sorry, but email is already taken! Try again!')
                    return redirect(url_for('register_page'))
                else:
                    break
            password = str(hashlib.md5(str(form.password.data).encode()).hexdigest())
            created = datetime.utcnow()
            admin = False
            key = form.key.data
            query = settings.find({})
            for data in query:
                if key in data.values():
                    index = list(data.values()).index(key)
                    keys = list(data.keys())[index]
                    rank = keys
                    session['rank'] = rank
                    if rank == 'worker1':
                        rank_show = 'Precinct'
                    elif rank == 'worker3':
                        rank_show = 'Prosecutor'
                    elif rank == 'worker2.1':
                        rank_show = 'Killing Investigator'
                    elif rank == 'worker2.2':
                        rank_show = 'Theft Investigator'
                    elif rank == 'worker2.3':
                        rank_show = 'Abduction Investigator'

                else:
                    flash('Key entered incorrectly! Contact the main office to confirm the validity of the key!')
                    return redirect(url_for('register_page'))
            session['username'] = username
            session['password'] = password


            user_id = db.insert_one({
                'username': username,
                'rank': rank,
                'rank_Show': rank_show,
                'email': email,
                'password': password,
                'created': created,
                'admin': admin,
            })

            flash('Thanks for registering')
            return redirect('/profile')

        return render_template("register.html", form=form)


"""
Views controller
"""
from functools import wraps
from flask import flash, render_template
from flask import request, redirect, url_for, session

from app import app, user_instance, bucket, bucket_item


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('home'))
    return wrap


@app.route('/dashboard')
@login_required
def dashboard():
    """
    Dashboard
    """
    email = session['email']
    user_id = user_instance.get_userid(email)
    buckets = bucket.get_users_buckets(user_id)
    return render_template('dashboard.html', data=buckets)


@app.route('/')
def home():
    """
    Home page
    """
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    This function registers a user if the user does not exist
    """
    error = None

    # check if the request method is post
    if request.method == "POST":
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        confirm_password = request.form['confirm_password'].strip()

        # check if password and password confirmation match
        if password == '' or email == '':
            error = 'Email and password can not be empty!'
            return render_template('signup.html', error=error)

        elif password != confirm_password:
            error = 'Password Mismatch! Please try again'
            return render_template('signup.html', error=error)

        # check if the password is alphanumeric
        elif user_instance.check_password_is_alphnum(password) is False:
            error = 'Password can only contain alhphanumeric characters'
            return render_template('signup.html', error=error)

        # check if password length is greater than six characters
        elif len(password) <= 6:
            error = "Password Should have more than six characters"
            return render_template('signup.html', error=error)

        # check if a user with that email exists
        elif user_instance.check_user_exists(email) is True:
            error = 'A user already exists with similar email'
            return render_template('signup.html', error=error)

        # create a new user
        else:
            user_instance.create_user(email, password)
            flash('Registration successful. Sign in into your Account')
            return redirect(url_for('home'))

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login a user
    """
    # Check the request  method
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check for empty input
        if password == '' or email == '':
            error = "PLease enter your email and password"
            return render_template('index.html', error=error)

        # Check if user exists
        elif user_instance.check_user_exists(email) is False:
            error = "Email does not exist. Please sign up"
            return render_template('index.html', error=error)

        # Login a user
        elif user_instance.login(email, password) is True:
            session['email'] = request.form['email']
            session['logged_in'] = True
            flash("You have successfully logged in!")
            return redirect(url_for('dashboard'))

        # Return error for incorrect password
        else:
            error = "Incorrect password"
            return render_template('index.html', error=error)
    return render_template('index.html')


@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    """
    Create a bucketlist
    """
    if request.method == 'POST':
        name = request.form['bucketlist_name']

        # Check if name is empty
        if name.strip() == '':
            error = "Bucket list name can not be empty"
            return render_template('create.html', error=error)

        # Check if name is alphanumeric
        elif name.str() is False:
            error = "Bucket list name can not Contain special characters"
            return render_template('create.html', error=error)

        # check if a buckelist with similar name exists
        elif bucket.check_if_bucketlist_exists(name) is True:
            error = "Bucketlist with similar name already exists"
            return render_template('create.html', error=error)
        else:
            # Create a bucketlist
            email = session['email']
            user_id = user_instance.get_userid(email)
            bucket.create_bucketlist(name, user_id)
            flash("You have successfully created a bucketlist")
            return redirect(url_for('dashboard'))

    return render_template('create.html')


@app.route('/rename', methods=['GET', 'POST'])
@login_required
def rename():
    """
    Rename a bucketlist
    """
    # if user is posting data
    if request.method == "POST":

        # get data from rename form
        name = request.form['name']
        title = request.form['title']
        print(name, title)

        # check if name field is empty
        if name.strip() == '':
            flash("Bucket list name can not be empty")

        # Check if name is alphanumeric
        elif name.isalnum() is False:
            flash("Bucketlist name cannot contain special characters")

        # check if name already exists
        elif bucket.check_if_bucketlist_exists(name) is True:
            flash("Bucketlist with similar name already exists")

        # Rename buckketlist
        else:
            bucket.rename(title, name)
            flash("You have renamed your bucketlist")

    return redirect(url_for('dashboard'))


@app.route('/delete/<title>')
@login_required
def delete(title):
    """
    Delete a bucketlist
    """
    # Delete bucketlist using title as name
    bucket.delete(title)
    flash("You have deleted your bucketlist")
    return redirect(url_for('dashboard'))


@app.route('/remove_item/<title>')
@login_required
def remove_item(title):
    """
    Remove an item from a bucketlist
    """
    # get email fro the session
    email = session['email']
    print(email)
    # get user's id using their email
    user_id = user_instance.get_userid(email)

    # remove item from bucketlist and return bucketlist name
    name = bucket_item.remove_item(user_id, title)
    flash("Bucketlist activity deleted")
    return redirect(url_for('get_bucketname', title=name))


@app.route('/mark_complete/<title>')
@login_required
def mark_complete(title):
    """
    Mark a bucketlist as complete
    """
    # Change bucketlist status to incomplete
    bucket.mark_as_complete(title)
    flash("Congratulations on completing " + title + " Bucket list")
    return redirect(url_for('dashboard'))


@app.route('/newbucketlists')
@login_required
def latest_buckets():
    """
    This returns three latest bucketlists a user has creates
    """
    email = session['email']
    user_id = user_instance.get_userid(email)

    # Get latest bucketlist
    latest = bucket.latest_bucketlists(user_id)
    return render_template('latest.html', data=latest)


@app.route('/completed')
@login_required
def completed():
    """
    Returns completed bucketlists
    """
    email = session['email']
    user_id = user_instance.get_userid(email)

    # completed bucketlists of a given user
    completed_buckets = bucket.completed_bucketlist(user_id)
    return render_template('completed.html', data=completed_buckets)


@app.route('/inprogress')
@login_required
def inprogress():
    """
    Returns bucketlists whose status is 'inprogress'
    """
    email = session['email']
    user_id = user_instance.get_userid(email)

    # in progress bucketlists of a given user
    inprogress_buckets = bucket.inprogress_bucketlist(user_id)
    return render_template('inprogress.html', data=inprogress_buckets)


@app.route('/add_activity', methods=['GET', 'POST'])
@login_required
def add_activity():
    """
    Add activity to a bucketlist
    """

    # Check if user is posting data
    if request.method == "POST":
        item = request.form['activity']

        # Name o the bucketlist
        name = request.form['title']

        # Get items of the bucketlist
        items = bucket_item.get_bucket_items(name)

        # Check if an item with similar name exists
        if item in items:
            flash("Activity already exists")

        # Check if item is blank
        elif item.strip() == '':
            flash("Activity can not be empty")

        # Add activity to bucketlist
        else:
            bucket_item.add_activity(name, item)
            flash("Activity added successfuly")

        return redirect(url_for('get_bucketname', title=name))


@app.route('/add_activity/<title>')
@login_required
def get_bucketname(title):
    """
    Returns bucketname and its activiteis(items)
    """
    # Get items of a bucketlist
    items = bucket_item.get_bucket_items(title)

    # create a list of dictionaries for these items
    print(items)
    return render_template("add_activity.html", data=items, title=title)


@app.route('/logout')
@login_required
def logout():
    """
    Logout a user
    """
    # remove a user from session
    session.pop('logged_in', None)
    flash('You have successfully loged out')
    return redirect(url_for('home'))

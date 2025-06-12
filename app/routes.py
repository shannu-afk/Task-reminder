from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify

main = Blueprint('main', __name__)

# Dummy user store and task storage for demonstration only!
USERS = {}
TASKS = {}  # key: username, value: list of task dicts

# ---------- AUTH ROUTES ----------

@main.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USERS and USERS[username] == password:
            session['user'] = username
            return redirect(url_for('main.dashboard'))
        else:
            error = 'Invalid username or password.'
    return render_template('login.html', error=error)

@main.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in USERS:
            error = 'Username already exists.'
        else:
            USERS[username] = password
            TASKS[username] = []
            flash('Account created! Please log in.')
            return redirect(url_for('main.login'))
    return render_template('register.html', error=error)

@main.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully.')
    return redirect(url_for('main.login'))

# ---------- DASHBOARD AND TASK ROUTES ----------

@main.route('/')
@main.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('main.login'))
    username = session['user']
    user = {'username': username}
    tasks = TASKS.get(username, [])
    return render_template('dashboard.html', user=user, tasks=tasks)

@main.route('/add_task', methods=['POST'])
def add_task():
    if 'user' not in session:
        return redirect(url_for('main.login'))
    username = session['user']
    title = request.form['title']
    time_slot = request.form['time_slot']
    duration = request.form['duration']
    # Generate a unique id for each task
    next_id = 1
    if TASKS[username]:
        next_id = max(t['id'] for t in TASKS[username]) + 1
    task = {
        'id': next_id,
        'title': title,
        'time_slot': time_slot,
        'duration': duration
    }
    TASKS[username].append(task)
    return redirect(url_for('main.dashboard'))

@main.route('/delete_task/<int:task_id>', methods=['GET', 'POST', 'DELETE'])
def delete_task(task_id):
    if 'user' not in session:
        return redirect(url_for('main.login'))
    username = session['user']
    tasks = TASKS.get(username, [])
    TASKS[username] = [task for task in tasks if task['id'] != task_id]
    # For AJAX requests, return 204 No Content
    if request.method in ['POST', 'DELETE']:
        return '', 204
    return redirect(url_for('main.dashboard'))
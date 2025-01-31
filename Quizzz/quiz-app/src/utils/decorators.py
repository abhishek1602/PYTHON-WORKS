from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('You need to log in first.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'role' in session and session['role'] != 'admin':
            flash('You do not have permission to access this page.')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

def timed_route(timeout):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # Logic to handle timing can be implemented here
            return f(*args, **kwargs)
        return decorated_function
    return decorator
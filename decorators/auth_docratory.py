'''
decorator to ensure user is logged in order to access protected route
'''

def authorize(orignal_func):
    from app import app, request, render_template
    from functools import wraps
    @wraps(orignal_func)
    def wrapper(*args, **kwargs):
        user = request.cookies.get('user')
        if user:
            return orignal_func(*args, **kwargs)
        else:
            return render_template(app.config['login_template'])
    return wrapper
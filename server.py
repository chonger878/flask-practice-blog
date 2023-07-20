from flask_app import app
from flask import render_template,redirect

@app.route('/')
def login():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/posts/add_post')
def add_post():
    return render_template('create_post.html')

@app.route('/posts/create')
def create_post():
    return redirect('/dashboard')

if __name__ == '__main__':
    app.run(debug=True)
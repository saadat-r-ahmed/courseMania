from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)


# ! HOMEPAGE CONTAINING 3 LINKS TO 3 PAGES
@app.route('/')
@app.route('/home')
@app.route('/homepage')
def homepage():
    return render_template('home.html')

# ! ALL LOGIN PAGES
@app.route('/student_login')
def student_login():
    return render_template('student_login.html')

@app.route('/teacher_login')
def teacher_login():
    return render_template('teacher_login.html')

@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')

# ! ALL PAGE LOGIN AUTHENTICATOR


# ! FLASH ERROR IN A NEW PAGE





if __name__ == '__main__':
    app.run(debug = True)

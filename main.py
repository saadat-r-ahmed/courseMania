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
@app.route('/admin_authinticate', methods = ['GET', 'POST'])
def admin_authinticate():
    if request.method == "POST":
        adminID = request.form["adminid"]
        password = request.form["password"]
        typ = str(type(adminID))
        return render_template('show_message.html', message = adminID+' '+password)
    
    if request.method == "GET":
        if 'adminID' in request.args:
            adminID = request.args["adminid"]
            password = request.args["password"]
            return render_template('show_message.html', message = adminID+' '+password)

@app.route('/student_authinticate', methods = ['GET', 'POST'])
def student_authinticate():
    if request.method == "POST":
        studentID= request.form["studentid"]
        password = request.form["password"]
        return render_template('show_message.html', message = 'Studnet getting ready')
    
    if request.method == "GET":
        if 'studentid' in request.args:
            studentID = request.args["studentid"]
            password = request.args["password"]
            return render_template('show_message.html', message = 'Studnet getting ready')        



@app.route('/teacher_authinticate', methods = ['GET', 'POST'])
def teacher_authinticate():
    if request.method == "POST":
        teacherID= request.form["teacherid"]
        password = request.form["password"]
        return render_template('show_message.html', message = 'Teacher getting ready')
    
    if request.method == "GET":
        if 'teacherid' in request.args:
            teacherID = request.args["teacherid"]
            password = request.args["password"]
            return render_template('show_message.html', message = 'Teacher getting ready')
    

        
# ! FORGOTTEN PASSWORD
@app.route('/forgotten_password')
def forgotten_password():
    return render_template('forgotten_password.html')


# ! FLASH ERROR IN A NEW PAGE



if __name__ == '__main__':
    app.run(debug = True)

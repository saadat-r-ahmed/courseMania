from flask import Flask, render_template, url_for, request, redirect, session, json
import admin
from flask_mysqldb import MySQL,MySQLdb #pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb
from datetime import datetime
# from mod.sql import sql
from sql import sql
from sql import insert_into_teacher

app = Flask(__name__)
app.secret_key = "caircocoders-ednalan-2020"
  
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cse370_project'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


# ! HOMEPAGE CONTAINING 3 LINKS TO 3 PAGES
@app.route('/')
@app.route('/home')
@app.route('/homepage')
def homepage():
    return render_template('home.html', title_bar = "Homepage")

# ! ALL LOGIN PAGES
@app.route('/student_login')
def student_login():
    return render_template('student_login.html', title_bar = "Student Login")

@app.route('/teacher_login')
def teacher_login():
    return render_template('teacher_login.html', title_bar = "Teacher Login")

@app.route('/admin_login')
def admin_login():
    if 'admin_id' in session:
        return redirect(url_for('admin_dashboard', admin_id =  session['admin_id']))
    return render_template('admin_login.html', title_bar = "Admin Login")


# ! ALL PAGE LOGIN AUTHENTICATOR
@app.route('/admin_authinticate', methods = ['GET', 'POST'])
def admin_authinticate():
    if request.method == "POST":
        adminID = request.form["adminid"]
        password = request.form["password"]
        return admin.authenticate_admin(adminID, password)
    
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


# ! DASHBOARD AFTER AUTHINTICATION

# admin dashboard
@app.route('/admin_dashboard/<admin_id>')
def admin_dashboard(admin_id):
    if 'admin_id' in session:
        user = session['admin_id']
        password = session['admin_password']
        return render_template('admin_dashboard.html', 
                               title_bar = 'Admin Dashboard: '+user, 
                               admin_id = user,
                               admin_name = session['admin_name']
                               )
    else:
        return render_template('show_message.html', message = 'The session ended')


# admin logout
@app.route('/logout')
def logout():
    session.pop('admin_id', None)
    session.pop('admin_password', None)
    session.pop('admin_name', None)
    session.pop('admin_email', None)
    return redirect(url_for('admin_login'))


# editing student
@app.route('/admin_dashboard/edit_student')
def edit_student():
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        result = cur.execute("SELECT * FROM student")
        students = cur.fetchall()
        return render_template('admin_edit_student.html', 
                               students=students, 
                               title_bar = 'Student editorial',
                               admin_id = session['admin_id']
                               )

@app.route('/updatesutdent', methods=['POST'])
def updatesutdent():
        pk = request.form['pk']
        name = request.form['name']
        value = request.form['value']
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if name == 'name':
           cur.execute("UPDATE student SET name = %s WHERE student_id = %s ", (value, pk))
        elif name == 'email':
           cur.execute("UPDATE student SET email = %s WHERE student_id = %s ", (value, pk))
        elif name == 'password':
           cur.execute("UPDATE student SET password = %s WHERE student_id = %s ", (value, pk))
        elif name == 'administer':
           cur.execute("UPDATE student SET administer = %s WHERE student_id = %s ", (value, pk))
        mysql.connection.commit()
        cur.close()
        return json.dumps({'status':'OK'})



# edit teacher
@app.route('/admin_dashboard/edit_teacher')
def edit_teacher():
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        result = cur.execute("SELECT * FROM teacher")
        teachers = cur.fetchall()
        
        return render_template('admin_edit_teacher.html', 
                               teachers=teachers, 
                               title_bar = 'Teacher editorial',
                               admin_id = session['admin_id']
                               )

@app.route('/updateteacher', methods=['POST'])
def updateteacher():
    pk = request.form['pk']
    name = request.form['name']
    value = request.form['value']
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if name == 'name':
        cur.execute("UPDATE teacher SET name = %s WHERE teacher_id = %s ", (value, pk))
    elif name == 'email':
        cur.execute("UPDATE teacher SET email = %s WHERE teacher_id = %s ", (value, pk))
    elif name == 'password':
        cur.execute("UPDATE teacher SET password = %s WHERE teacher_id = %s ", (value, pk))
    elif name == 'administer':
        cur.execute("UPDATE teacher SET appointed_by = %s WHERE teacher_id = %s ", (value, pk))
    mysql.connection.commit()
    cur.close()
    return json.dumps({'status':'OK'})


# appint teacher
@app.route('/admin_dashboard/appoint_teacher')
def appoint_teacher():
    return render_template('admin_assign_teacher.html')

@app.route('/createteacher', methods=['POST'])
def createteacher():
    if 'admin_id' in session:
        id = request.form['teacher_id']
        name = request.form['teacher_name']
        email = request.form['teacher_email']
        password = request.form['teacher_password']
        appointed_by = session['admin_id']
        
        
        chq = f'select * from teacher where teacher_id = "{id}";'
        chq = sql(chq)      
        if len(chq) > 0:
            return render_template('show_message.html', message = 'Teacher Already Exists')
        else:
            insert_into_teacher(id, name, email, password, appointed_by)
            return render_template('show_message.html', message = 'Teacher created')
    
    else:
        return render_template('show_message.html', message = 'The session ended')




if __name__ == '__main__':
    app.run(debug = True)

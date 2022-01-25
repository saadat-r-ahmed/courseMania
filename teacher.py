from flask import Flask, render_template, url_for, request, redirect, session
# from main import app
from mod.sql import sql

# ! THE TEACHER CREDENTIALS ARE AUTHINTICATED !
def authenticate_teacher(id, pw):
    qry = f"SELECT teacher_id, name, email, password FROM teacher WHERE teacher_id = '{id}' and password = '{pw}' "
    tab = sql(qry)
    print(tab)
    # the teacher user does not exist
    if len(tab) == 0:
        msg = 'Id or Password does not exit in teacher database.'
        return render_template("show_message.html", title_bar = "Admin Login Failed",  message = msg)
    
    # the admin user exists
    else:
        teacher_id, name, email, password = tab[0][0], tab[0][1], tab[0][2], tab[0][3]
        session['teacher_id'] = teacher_id
        session['teacher_password'] = password
        session['teacher_name'] = name
        session['teacher_email'] = email
        return redirect(url_for('teacher_dashboard' , teacher_id = teacher_id))
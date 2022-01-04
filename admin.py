from flask import Flask, render_template, url_for, request, redirect, session
from main import app
from mod.sql import sql

# ! THE ADMIN CREDENTIALS ARE AUTHINTICATED !
def authenticate_admin(id, pw):
    qry = f"SELECT id, name, email, password FROM admin WHERE id = '{id}' and password = '{pw}' "
    tab = sql(qry)
    print(tab)
    # the admin user does not exist
    if len(tab) == 0:
        msg = 'Id or Password or both not registered as admin.'
        return render_template("show_message.html", title_bar = "Admin Login Failed",  message = msg)
    
    # the admin user exists
    else:
        admin_id, name, email, password = tab[0][0], tab[0][1], tab[0][2], tab[0][3]
        session['admin_id'] = admin_id
        session['admin_password'] = password
        session['admin_name'] = name
        session['admin_email'] = email
        return redirect(url_for('admin_dashboard' , admin_id = admin_id))
    
    
# # ! THE ADMIN DASHBOARD IS GENERATED !
# @app.route('/admin_dashboard')
# def admin_dashboard():
#     admin_id = 101
#     print('point2', admin_id)
#     # the admin user exists
#     msg = f'{admin_id}'
#     return render_template("admin_dashboard.html", title_bar = "Admin Login Complete",  message = msg)
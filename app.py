from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
#    return 'Hello World!'

#this will be our login page eventually
    return '<a href="/admin">admin stuff</a> <br> <a href="/employee">employee stuff</a>'
#

@app.route('/admin')
def admin_home():
    return render_template('admin/home.html') #this should work properly??
    #templates/admin/home ?


@app.route('/admin/sales')
def sales():
    return render_template('admin/sales.html') #this should work properly??
    #templates/admin/home ?

@app.route('/admin/users')
def users():
    return render_template('admin/users.html') #this should work properly??
    #templates/admin/home ?


@app.route('/employee')
def employee_home():
    return render_template('employee/home.html')
    #templates/employee/home ?

@app.route('/employee/item')
def item():
    return render_template('employee/item.html') #this should work properly??
    #templates/admin/home ?

@app.route('/logout')
def logout():
    #want to clear any cookies/caching we do

    return render_template('login.html')

@app.route('/logout')
def logout():
    #want to clear any cookies/caching we do

    return render_template('login.html')    

if __name__ == '__main__':
    app.run()

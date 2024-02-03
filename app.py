from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
#    return 'Hello World!'

#this will be our login page
    return '<a href="/admin/home.html">admin stuff</a> <br> <a href="/employee/home.html">employee stuff</a>'

@app.route('/admin')
def admin_home():
    render_template('admin/home.html') #this should work properly??

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, url_for, request, jsonify
import psycopg2
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
#    return 'Hello World!'

#this will be our login page eventually
    return '<a href="/admin">admin stuff</a> <br> <a href="/employee">employee stuff</a>'


@app.route('/testDB')
def test_db():  # put application's code here
    conn_string = "dbname=goodsole-inventorymanagement-database host=goodsole-inventorymanagement-server.postgres.database.azure.com port=5432 sslmode=require user=lfmxqslkgr password={password}"
    conn = psycopg2.connect(conn_string)
    conn.close()
    return ("Connection established")


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

@app.route('/admin/item')
def sku_search():
    return render_template('admin/item.html')

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

@app.route('/get_item/<barcode>')
def get_item(barcode):

    #SQL query to get item with barcode from database
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run()

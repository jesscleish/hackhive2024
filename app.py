import psycopg2
from flask import Flask, render_template, jsonify, redirect, url_for, request, session, flash

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    #    return 'Hello World!'
    session['user'] = 1
    # this will be our login page eventually
    #return '<a href="/admin">admin stuff</a> <br> <a href="/employee">employee stuff</a>'
    return render_template("login.html")

@app.route('/testDB')
def test_db():  # put application's code here
    conn_string = "dbname=goodsole-inventorymanagement-database host=goodsole-inventorymanagement-server.postgres.database.azure.com port=5432 sslmode=require user=lfmxqslkgr password={password}"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    # Drop previous table of same name if one exists

    cursor.execute("DROP TABLE IF EXISTS inventory;")
    cursor.execute("DROP TABLE IF EXISTS transactions")
    cursor.execute("DROP TABLE IF EXISTS users;")
    text += ("Finished dropping table (if existed)")

    # Create a table

    cursor.execute(
        "CREATE TABLE inventory (    SKU INTEGER PRIMARY KEY,    ShoeName VARCHAR(100),    Brand VARCHAR(100),    Type VARCHAR(100),    Gender BOOLEAN,    Size SMALLINT,    Price DOUBLE PRECISION,    QuantityInStock INTEGER,    SaleCategory DOUBLE PRECISION,    Color VARCHAR(50));")
    cursor.execute(
        "CREATE TABLE transactions (    TimeCompleted TIMESTAMP,    OrderNumber INTEGER PRIMARY KEY,    ItemSKU INTEGER,    Value DOUBLE PRECISION);")
    cursor.execute("CREATE TABLE users (    username VARCHAR(100),    password VARCHAR(100),    isAdmin bit);")
    text += ("Finished creating table")

    # Insert some data into the table

    cursor.execute("INSERT INTO inventory (SKU, ShoeName) VALUES (%s, %s);", (1, "Nike"))
    cursor.execute("INSERT INTO inventory (SKU, ShoeName) VALUES (%s, %s);", (2, "New Balance"))
    cursor.execute("INSERT INTO inventory (SKU, ShoeName)VALUES (%s, %s);", (3, "Adidas"))
    text += ("Inserted 3 rows of data")


    cursor.execute("SELECT * FROM inventory;")

    try:
    # fetching all the rows
        rows = cursor.fetchall()
        try:
            text+=str(len(rows))
            for row in rows:
                text = ("Data row = (%s, %s, %s)" % (str(row[0]), str(row[1]), str(row[2])))
        except:
            text+= "failed to parse len of a list"
    except:
        text+="failed to get result"



    conn.commit()
    cursor.close()
    conn.close()
    text += ("Connection closed")
    return text


@app.route('/admin')
def admin_home():
    if not isAdmin():
        flash(f'You must be an admin.', 'warning')
        return redirect(url_for('hello_world'))
    return render_template('admin/home.html')  # this should work properly??
    # templates/admin/home ?


@app.route('/admin/sales')
def sales():
    if not isAdmin():
        flash(f'You must be an admin.', 'warning')
        return redirect(url_for('hello_world'))
    return render_template('admin/sales.html')  # this should work properly??
    # templates/admin/home ?


@app.route('/admin/users')
def users():
    if not isAdmin():
        flash(f'You must be an admin.', 'warning')
        return redirect(url_for('hello_world'))
    return render_template('admin/users.html')  # this should work properly??
    # templates/admin/home ?

@app.route('/admin/addUser', methods=['POST'])
def addUser():
    if not isAdmin():
        flash(f'You must be an admin.', 'warning')
        return redirect(url_for('hello_world'))

    username = request.form.get('fUsername')
    password = request.form.get('fPassword')

    # add to db posted information


@app.route('/admin/item')
def sku_search():
    if not isAdmin():
        flash(f'You must be an admin.', 'warning')
        return redirect(url_for('hello_world'))
    return render_template('admin/item.html')


@app.route('/employee')
def employee_home():
    #if not isLoggedIn():
     #   flash(f'You must be logged in.', 'warning')
     #   return redirect(url_for('hello_world'))
    return render_template('employee/home.html')
    # templates/employee/home ?


@app.route('/employee/item')
def item():
    if not isLoggedIn():
        flash(f'You must be logged in.', 'warning')
        return redirect(url_for('hello_world'))
    return render_template('employee/item.html')  # this should work properly??
    # templates/admin/home ?


@app.route('/login2', methods=['POST'])
def login2():
    username = request.form.get('fUsername')
    password = request.form.get('fPassword')
    session['username'] = username

    if username == "admin" and password == "admin":
        session['user'] = 1
        return render_template('admin/home.html')

    if username == "" and password == "":
        session['user'] = 1
        return render_template('admin/home.html')

    if username == "emp" and password == "emp":
        session['user'] = 0
        return render_template('employee/home.html')

    return render_template('login.html')  # maybe add some sort of message

@app.route('/login', methods=['GET'])
def login3():
    return render_template('login.html')
@app.route('/login', methods=['POST'])
def login():

    username = request.form.get('fUsername')
    password = request.form.get('fPassword')
    success = False
    session['username'] = username

    if username == "admin" and password == "admin":
        session['user'] = 1
        return render_template('admin/home.html')

    if username == "" and password == "":
        session['user'] = 1
        return render_template('admin/home.html')

    if username == "emp" and password == "emp":
        session['user'] = 0
        return render_template('employee/home.html')

    # now check against our own database
    #check if username is in db, if no redirect to login pg
    db_user =""
    #if username in db, check password against stored password
    db_pass = ""

    if success:
        #check what user status associated with username
        db_user_status =""
        session['username'] = username
        if db_user_status == 1:
            session['user'] = 1
            return render_template('admin/home.html')
        else:
            session['user'] = 0
            return render_template('employee/home.html')

    return render_template('login.html') #maybe add some sort of message

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/get_item/<barcode>')
def get_item(barcode):
    # SQL query to get item with barcode from database
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404


def isLoggedIn():
    try:
        if session['user'] == 1:
            return True
        elif session['user'] == 0:
            return True
        else:
            return False
    except:
        return False

def isAdmin():
    try:
        if session['user'] == 1:
            return True
        else:
            return False
    except:
        return False

if __name__ == '__main__':
    # Quick test configuration. Please use proper Flask configuration options
    # in production settings, and use a separate file or environment variables
    # to manage the secret key!
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run()

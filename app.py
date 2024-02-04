import psycopg2
from flask import Flask, render_template, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    #    return 'Hello World!'

    # this will be our login page eventually
    return '<a href="/admin">admin stuff</a> <br> <a href="/employee">employee stuff</a>'


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

    # Clean up

    sql = '''SELECT * FROM inventory;'''

    # executing the sql command
    cursor.execute(sql)
    try:
    # fetching all the rows
        results = cursor.fetchall()
        text += results
    except:
        text+="fail"

        
    conn.commit()
    cursor.close()
    conn.close()
    text += ("Connection closed")
    return text


@app.route('/admin')
def admin_home():
    return render_template('admin/home.html')  # this should work properly??
    # templates/admin/home ?


@app.route('/admin/sales')
def sales():
    return render_template('admin/sales.html')  # this should work properly??
    # templates/admin/home ?


@app.route('/admin/users')
def users():
    return render_template('admin/users.html')  # this should work properly??
    # templates/admin/home ?


@app.route('/admin/item')
def sku_search():
    return render_template('admin/item.html')


@app.route('/employee')
def employee_home():
    return render_template('employee/home.html')
    # templates/employee/home ?


@app.route('/employee/item')
def item():
    return render_template('employee/item.html')  # this should work properly??
    # templates/admin/home ?


@app.route('/logout')
def logout():
    # want to clear any cookies/caching we do

    return render_template('login.html')


@app.route('/get_item/<barcode>')
def get_item(barcode):
    # SQL query to get item with barcode from database
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404


if __name__ == '__main__':
    app.run()

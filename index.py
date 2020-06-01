from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

def get_connection():
    return pymysql.connect(host='******gear.host',
                             user='*****omapp',
                             password='*******',
                             db='*******',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/productos1')
def productos1():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM productos"
            cursor.execute(sql)
            productos = cursor.fetchall()
            productos = list(productos)
    finally:
            connection.close()

    return render_template('productos1.html', productos = productos)

if __name__ == '__main__':
        app.run(debug=True)
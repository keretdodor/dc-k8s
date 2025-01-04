from flask import Flask, render_template, request, redirect, url_for, Response
import mysql.connector
import os
from time import sleep

app = Flask(__name__)

def get_db_connection():
    max_retries = 5
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            connection = mysql.connector.connect(
                host=os.getenv('MYSQL_HOST'),
                user=os.getenv('MYSQL_USER'),
                password=os.getenv('MYSQL_PASSWORD', 'password'),
                database=os.getenv('MYSQL_DATABASE', 'employees_db')
            )
            return connection
        except mysql.connector.Error as err:
            retry_count += 1
            if retry_count == max_retries:
                raise err
            sleep(5)

@app.route('/healthy')
def health_check():
    try:
        return Response(status=200)
    except:
        return Response(status=500)

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM employees')
        employees = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('index.html', employees=employees)
    except Exception as e:
        return f"Database error: {str(e)}", 500

@app.route('/add', methods=['POST'])
def add_employee():
    try:
        name = request.form['name']
        role = request.form['role']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO employees (name, role) VALUES (%s, %s)', (name, role))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    except Exception as e:
        return f"Error adding employee: {str(e)}", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

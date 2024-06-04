from flask import Flask, render_template, request, redirect, url_for
import config
app = Flask(__name__)
#from flask_mysqldb import MySql 
#app.config['MYSQL_HOST'] = config.MYSQL_HOST
#app.config['MYSQL_USER'] = config.MYSQL_USER
#app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
#app.config['MYSQL_DB'] = config.MYSQL_DB

#mysql = MySql(app)


# List to store people data
people = []

@app.route('/')
def index():
    return redirect(url_for('add_person'))

@app.route('/add_person', methods=['GET', 'POST'])
def add_person():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']

       
        if name and age:
            people.append({'name': name, 'age': age})
           # cur = mysql.connection.cursor()
           # sql = "INSERT INTO person (name, age) VALUES ('$name',  '$age')"
           # data = (name, age)
           # cur.execute(sql, data)
           # mysql.connection.commit()  
            return redirect(url_for('view_people'))
    return render_template('add_person.html')

@app.route('/view_people')
def view_people():
    return render_template('view_people.html', people=people)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

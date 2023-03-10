from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

#DBconnection details
host='localhost'
username='root'
password='root'
scema='calculator'

def data_for_dropdown():
        #database connection
    conn = pymysql.connect(host='localhost', user='root', password='root', database='calculator')
    cursor = conn.cursor()

    # Get all subjects from the 'masterTable' table
    cursor.execute("SELECT EngineeringID,EngineeringName,EngineeringIcon FROM masterTable")
    data = cursor.fetchall()

    # Close database connection
    cursor.close()
    conn.close()

    return data


@app.route('/')
def index():
    master_rows=data_for_dropdown()
    return render_template("index.html",masters=master_rows)

@app.route('/calculatorList')
def calculatorList():
    # Get the subject ID from the request parameter
    E_id = request.args.get('E_id')

    # Connect to database
    conn = pymysql.connect(host='localhost', user='root', password='root', database='calculator')
    cursor = conn.cursor()

    # Get all students for the selected subject from the 'students' table
    cursor.execute("SELECT CalculatorName,CalculatorDiscription FROM subTable WHERE Sequence = %s", E_id)
    sub_rows = cursor.fetchall()

    master_rows=data_for_dropdown()

    # Close database connection
    cursor.close()
    conn.close()

    return render_template("calculatorList.html",subs=sub_rows,master_rows=master_rows)

@app.route('/about')
def about():
    master_rows=data_for_dropdown()
    return render_template("about.html",master_rows=master_rows)

@app.route('/contact')
def contact():
    master_rows=data_for_dropdown()
    return render_template("contact.html",master_rows=master_rows)

if __name__ == '__main__':
    app.run(debug=True)

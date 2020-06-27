from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, ReportForm
import mysql.connector as sql

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    try:
        conn = sql.connect(user='root', password='Son@123456',
                                host='localhost', database='miniproject')
        cursor = conn.cursor()
    except sql.Error as err:
        if err.errno == sql.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == sql.errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    hlabels = []
    hvalues = []

    hquery = """
        SELECT 
            timestamp, data_value 
        FROM 
            miniproject.sensor_data AS a INNER JOIN miniproject.sensor_header AS b ON a.sensor_header_id=b.id
        WHERE sensor_type="Humidity" AND sensor_status="Active" AND area_id=2 
        ORDER BY timestamp DESC LIMIT 10;
    """
    try:
        cursor.execute(hquery)
    except sql.Error as err:
        print(err)
    hdata = cursor.fetchall()
    while True:
        if len(hdata)>0:
            data = hdata.pop()
            hlabels.append(str(data[0]))
            hvalues.append(int(data[1]))
        else:
            break
    # for item in hdata:
    #     hlabels.append(str(item[0]))
    #     hvalues.append(int(item[1]))

    tlabels = []
    tvalues = []
    tquery = """
        SELECT 
            timestamp, data_value 
        FROM 
            miniproject.sensor_data AS a INNER JOIN miniproject.sensor_header AS b ON a.sensor_header_id=b.id
        WHERE sensor_type="Temperature" AND sensor_status="Active" AND area_id=2 
        ORDER BY timestamp DESC LIMIT 10;
    """
    try:
        cursor.execute(tquery)
    except sql.Error as err:
        print(err)
    tdata = cursor.fetchall()
    while True:
        if len(tdata)>0:
            data = tdata.pop()
            tlabels.append(str(data[0]))
            tvalues.append(int(data[1]))
        else:
            break
    # for item in tdata:
    #     tlabels.append(str(item[0]))
    #     tvalues.append(int(item[1]))

    llabels = []
    lvalues = []
    lquery = """
        SELECT 
            timestamp, data_value 
        FROM 
            miniproject.sensor_data AS a INNER JOIN miniproject.sensor_header AS b ON a.sensor_header_id=b.id
        WHERE sensor_type="Light" AND sensor_status="Active" AND area_id=2 
        ORDER BY timestamp DESC LIMIT 10;
    """
    try:
        cursor.execute(lquery)
    except sql.Error as err:
        print(err)
    ldata = cursor.fetchall()
    while True:
        if len(ldata)>0:
            data = ldata.pop()
            llabels.append(str(data[0]))
            lvalues.append(int(data[1]))
        else:
            break
    # for item in ldata:
    #     llabels.append(str(item[0]))
    #     lvalues.append(int(item[1]))

    colors = [
        "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
        "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
        "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

    hbar_labels=hlabels
    hbar_values=hvalues
    tbar_labels=tlabels
    tbar_values=tvalues
    lbar_labels=llabels
    lbar_values=lvalues
    return render_template('index.html', title='Home', user=user, posts=posts, hlabels=hbar_labels, hvalues=hbar_values
                                    , tlabels=tbar_labels, tvalues=tbar_values, llabels=lbar_labels, lvalues=lbar_values)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route("/report")
def report():
    return render_template('report.html')
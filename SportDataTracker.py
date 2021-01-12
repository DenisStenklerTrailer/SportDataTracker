from flask import Flask, render_template, request, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

@app.route('/DataCollector', methods=['GET','POST'])
def DataCollector():
    if request.method == 'POST':
        # do stuff when the form is submitted
        return redirect(url_for('DataCollector'))

    return render_template('DataCollector.html')

@app.route('/statistics', methods=['GET','POST'])
def statistics():
    if request.method == 'POST':
        # do stuff when the form is submitted
        return redirect(url_for('statistics'))

    return render_template('statistics.html')

@app.route("/submit", methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        SportType = request.form["SportType"]
        Distance = request.form["distance"]
        ElevationGain = request.form["ElevationGain"]
        Date = request.form["Date"]
        Time = request.form["Time"]

        print(SportType)

    return redirect('/')



if __name__ == '__main__':
    app.debug=True
    app.run()



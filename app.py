from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/name')
def name():
    return render_template('name.html')

@app.route('/age')
def age():
    return render_template('age.html')

@app.route('/school')
def school():
    return render_template('school.html')

@app.route('/hobby')
def hobby():
    return render_template('hobby.html')

@app.route('/countdown')
def countdown():
    return render_template('countdown.html')

@app.route("/fireworks")
def fireworks():
    return render_template("fireworks.html")


if __name__ == '__main__':
    app.run(debug=True)

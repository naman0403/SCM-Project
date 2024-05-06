#python for html
from flask import Flask, request, render_template

app = Flask(_name_)

def calculate_bmi(weight, height):
    bmi = weight / (height * height)
    return bmi

@app.route('/')
def index():
    return render_template('cal.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    weight = float(request.form['weight'])
    height = float(request.form['height'])

    bmi = calculate_bmi(weight, height)
    return render_template('result.html', bmi=bmi)

if _name_ == '_main_':
    app.run(debug=True)
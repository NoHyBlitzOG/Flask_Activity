from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/surprise')
def surprise():
    return render_template('surprise.html')

@app.route('/areaofcircle', methods=['GET','POST'])
def areaofcircle():
    result = None
    if request.method == 'POST':
        area_result = request.form.get('area_result', '')
        result = 3.14*int(area_result)**2
    return render_template('areaofcircle.html', result=result)

@app.route('/areaoftriangle', methods=['GET', 'POST'])
def areaoftriangle():
    result = None
    if request.method == 'POST':
        base = request.form.get('base', '')
        height = request.form.get('height', '')
        result = 0.5*float(base)*float(height)
    return render_template('areaoftriangle.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)

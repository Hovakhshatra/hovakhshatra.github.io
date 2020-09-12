from flask import Flask, render_template, url_for, request, session
app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "12345qpalzm123okmwsx"

Stock_name = ['AH', 'AY', 'AM', 'RR']
Stock_value = [12, 0.01, 20.5, -12.3]


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html', Stock_name=Stock_name, Stock_value=Stock_value)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, request
from olbot import bot



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def check():
    if request.method == 'POST' and 'checkin' in request.form:
        bot('checkin') #send message to telegram
    elif request.method == 'POST' and 'checkout' in request.form:
        bot('checkout') #send message to telegram
    else:
        return  'nope xD'
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

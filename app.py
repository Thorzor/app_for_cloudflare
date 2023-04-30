from flask import Flask, render_template
from checkout import get_payment_link

app = Flask(__name__)


@app.route('/')
def render_page():  # put application's code here
    # link = get_payment_link()
    return render_template('page.html', data=get_payment_link())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

import requests
from flask import Flask, render_template
from checkout import get_payment_link
import random

app = Flask(__name__)


@app.route('/')
def render_page():  # put application's code here
    URL = 'https://checkout-staging.begateway.com/ctp/api/checkouts'
    login = '1370'
    password = '4539d4343361874408977f874e428438c6468613a0a58ee9f266a90772f6ded0'
    data = {
        "checkout": {
            "test": False,
            "transaction_type": "payment",
            "attempts": 3,
            "settings": {
                "notification_url": "http://your_shop.com/notification",
                "language": "en",
                "customer_fields": {
                    "read_only": ["email"]
                },
                "credit_card_fields": {
                    "holder": "Rick Astley",
                    "read_only": ["holder"]
                }
            },
            "payment_method": {
                "types": ["credit_card"]
            },
            "order": {
                "currency": "USD",
                "amount": random.randint(100, 1000),
                "description": "Order description"
            },
            "customer": {
                "address": "Baker street 221b",
                "country": "GB",
                "city": "London",
                "email": "jake@example.com"
            }
        }
    }
    response = requests.post(URL, json=data, auth=(login, password))
    return render_template('page.html', data=response.json()['checkout']['redirect_url'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

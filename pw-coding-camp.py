from flask import Flask
from flask import render_template, redirect, url_for
from flask import request

app = Flask(__name__)

transactions = [
    {"id": 1, "subject": "Berliner Weissbier", "captured_amount": 20.0, "currency": "EUR", "amount": 30.0, "refundable_amount": 10.0},
    {"id": 2, "subject": "Zywiec Beer", "captured_amount": 50.0, "currency": "EUR", "amount": 50.0, "refundable_amount": 0.0},
    {"id": 3, "subject": "Tyskie", "captured_amount": 100, "currency": "USD", "amount": 100.0, "refundable_amount": 100.0}
]

@app.route('/refund', methods=['POST'])
def refund():
    for transaction in transactions:
        if transaction["id"] == int(request.form['transactionId']):
            transaction["refundable_amount"] = transaction["refundable_amount"] - float(request.form['refundAmount'])
    return redirect(url_for('index'))

@app.route('/capture', methods=['POST'])
def capture():
    for transaction in transactions:
        if transaction["id"] == int(request.form['transactionId']):
            transaction["captured_amount"] = transaction["captured_amount"] + float(request.form['captureAmount'])
    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html', transactions=transactions)


@app.context_processor
def context_processor():
    return dict(transactions=['transaction 1', 'transaction 2'])


if __name__ == '__main__':
    # debug=True makes it restart every time you make a change
    app.run(debug=True)

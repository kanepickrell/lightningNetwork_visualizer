from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the Flask app for the Bitcoin Lightning Network Dashboard.'

@app.route('/lightning')
def lightning_data():
    # Placeholder for fetching data from LND
    data = {"message": "This is where Lightning Network data will be served."}
    return data


if __name__ == '__main__':
    app.run(debug = True)


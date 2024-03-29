from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/sample")
def sample():
    sample_data = {
        'id': 'abc',
        'value': 123
    }
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

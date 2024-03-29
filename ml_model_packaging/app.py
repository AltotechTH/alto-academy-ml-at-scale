from flask import Flask, jsonify, request
from transformers import pipeline

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

# post request, recieving text and returning summarized text
@app.route("/summarize", methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text')
    if text is None:
        return jsonify({'error': 'text is required'})
    
    summarizer = pipeline("summarization", model="stevhliu/my_awesome_billsum_model")
    result = summarizer(text)
    
    return jsonify(result[0])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


from flask import Flask, render_template, jsonify, request
import sample_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    return jsonify(sample_data.data)

if __name__ == '__main__':
    app.run(debug=True)

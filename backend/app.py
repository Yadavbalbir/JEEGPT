from flask import Flask, request, jsonify
from flask_cors import CORS
from model import JEEGPT
app = Flask(__name__)
CORS(app)


@app.route('/api/jeegpt', methods=['POST'])
def process_data():
    data = request.get_json()
    # Process the data
    query = data['query']
    res = JEEGPT(query)
    result = {
        'message': res,
        'query': query
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run()

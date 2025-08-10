from bottle import Bottle, run, hook, response
import json

app = Bottle()

@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'

@app.route('/')
def hello():
    return {
        "message": "Hello, World!",
        "status": "running",
    }

@app.route('/api/data')
def get_data():
    mock_data = {
        "users": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
            {"id": 3, "name": "Charlie"}
        ],
        "count": 3
    }
    response.content_type = 'application/json'
    return json.dumps(mock_data)

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8081 , server='paste' , reloader=True)

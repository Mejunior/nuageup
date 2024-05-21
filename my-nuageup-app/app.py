from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World! V2"

@app.route('/healthz')
def healthz():
    # Logic to determine health; can be as simple or complex as needed
    # Here we just return a simple HTTP 200 response
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

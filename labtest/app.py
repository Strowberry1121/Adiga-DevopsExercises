from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/bright-hawk-46', methods=['GET'])
def info():
    return jsonify({"info": "Service is live"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
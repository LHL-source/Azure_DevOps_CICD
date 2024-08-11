from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/power/<int:x>/<int:y>')
def power(x, y):
    result = x ** y
    print("today is 7-6-2024 V5")
    return jsonify(result=result)  # Return a JSON response with the result

@app.route('/health_V2')
def health_check():
    # Check if application components are healthy
    # Return a JSON response indicating health status
    return jsonify(status='ok')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)

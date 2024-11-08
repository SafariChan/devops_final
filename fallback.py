<<<<<<< HEAD
from flask import Flask, request, jsonify

app = Flask(__name__)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@app.route('/fib', methods=['GET'])
def fibonacci():
    n = int(request.args.get('n', 10))
    return jsonify({'result': fib(n)})

if __name__ == "__main__":
=======
from flask import Flask, request, jsonify

app = Flask(__name__)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@app.route('/fib', methods=['GET'])
def fibonacci():
    n = int(request.args.get('n', 10))
    return jsonify({'result': fib(n)})

if __name__ == "__main__":
>>>>>>> 984116590b372c42be01395146a901379956eda7
    app.run(host="0.0.0.0", port=5000)
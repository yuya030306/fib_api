from flask import Flask, request, jsonify

app = Flask(__name__)

def fibonacci(n):
    if n == 1 or n == 2:  
        return 1
    a, b = 1, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b  


@app.route('/fib', methods=['GET'])
def get_fibonacci():
    try:
        n = request.args.get('n', type=int)

        if n is None or n <= 0:
            return jsonify({"status": 400, "message": "Please enter a positive integer."}), 400
        
        result = fibonacci(n)
        return jsonify({"result": result}), 200
    
    except Exception as e:
        return jsonify({"status": 500, "message": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)

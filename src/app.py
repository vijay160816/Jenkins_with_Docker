from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return "Welcome to Jenkins + Docker Demo App!"

# Health check route
@app.route("/health")
def health():
    return jsonify(status="UP", message="Service is healthy")

# Dynamic greeting route
@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}! This app is running inside Docker, deployed by Jenkins."

# Simple calculator API
@app.route("/add", methods=["GET"])
def add_numbers():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify(operation="addition", a=a, b=b, result=a+b)
    except ValueError:
        return jsonify(error="Invalid input, please provide integers"), 400

# List of items (mock database)
items = ["apple", "banana", "cherry"]

@app.route("/items", methods=["GET", "POST"])
def manage_items():
    if request.method == "GET":
        return jsonify(items=items)
    elif request.method == "POST":
        new_item = request.json.get("item")
        if new_item:
            items.append(new_item)
            return jsonify(message="Item added", items=items), 201
        return jsonify(error="No item provided"), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)


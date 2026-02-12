from flask import Flask, jsonify, request

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return """
    <h1>Welcome to Jenkins + Docker Demo App!</h1>
    <p>This is a sample Flask application deployed with Jenkins and Docker.</p>
    <ul>
        <li><a href="/health">Health Check</a></li>
        <li><a href="/hello/World">Say Hello</a></li>
        <li><a href="/items">View Items</a></li>
    </ul>
    <h2>Calculator</h2>
    <form action="/add" method="get">
        <label for="a">First number:</label>
        <input type="text" id="a" name="a" required>
        <br><br>
        <label for="b">Second number:</label>
        <input type="text" id="b" name="b" required>
        <br><br>
        <input type="submit" value="Add">
    </form>
    """

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


from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/name", methods=["GET"])
def Name():
    """
    Returns the string "Hello, world" to the caller
    """
    name = {
        "name": "Rich"
    }
    return jsonify(name)

@app.route("/hello/<name>", methods=["GET"])
def helloName(name):
    """
    Returns the data dictionary below to the caller as JSON
    """
    hello = {
        "messege": "hello{0}".format(name)
    }
    return jsonify(hello)

@app.route("/distance", methods=["POST"])
def dis():
    r = request.get_json()
    dis_x = abs(r["a"][0] - r["b"][0])
    dis_y = abs(r["a"][1] - r["b"][1])
    real_dis = (dis_x**2 + dis_y**2)**0.5

    res = {
        "distance": "{0}".format(real_dis),
        "a": r["a"],
        "b": r["b"]
    }
    return jsonify(res), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1")
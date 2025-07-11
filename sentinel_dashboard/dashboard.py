import json
import os

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

LOGS_PATH = "data/logs.json"


@app.route("/")
def index():
    if os.path.exists(LOGS_PATH):
        with open(LOGS_PATH, "r") as f:
            logs = json.load(f)
    else:
        logs = []
    return render_template("index.html", logs=logs)


@app.route("/alerts")
def alerts():
    # Placeholder for alert fetching logic
    return jsonify([])


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if file:
        filepath = os.path.join("data", file.filename)
        file.save(filepath)
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "fail"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, request, jsonify
from datetime import datetime



app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "ok", "message": "HeadsIn API is running", "timestamp": datetime.now().isoformat()})

@app.route("/get-ip", methods=["GET"])
def get_ip():
    # Check if behind a proxy/load balancer
    if request.headers.get("X-Forwarded-For"):
        ip = request.headers.get("X-Forwarded-For").split(',')[0]  # Take the first IP
    else:
        ip = request.remote_addr  # Direct connection

    return jsonify({"ip": ip})

if __name__ == "__main__":
    app.run(debug=True)

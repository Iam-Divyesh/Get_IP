import geocoder
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "ok", "message": "HeadsIn API is running"})

@app.route("/get-ip", methods=["GET"])
def get_ip():
    # Get the client's IP address from request headers
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # Get location details using geocoder
    g = geocoder.ip(client_ip)
    
    return jsonify({
        "ip": client_ip,
        "city": g.city,
        "country": g.country,
        "latlng": g.latlng
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

import socket
from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
      return jsonify({"status": "ok", "message": "HeadsIn API is running"})
    

@app.route('/get-ip', methods=['GET'])
def get_ip():
    host_name = socket.gethostname()

    ip_address = socket.gethostbyname(host_name)

    print(host_name)
    print(ip_address)

    return jsonify({'ip': ip_address, 'hostname': host_name})

if __name__ == '__main__':
    app.run(debug=True,port=5000)

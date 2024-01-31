from flask import Flask, render_template, jsonify
from threading import Thread
import socket

app = Flask(__name__)

received_data = ""

def start_socket_server():
    global received_data
    HOST = '0.0.0.0'
    PORT = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Add this line
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Listening on {HOST}:{PORT}")

    conn, addr = server.accept()
    print(f"Connected to {addr}")

    try:
        while True:
            data = conn.recv(1024)
            if data:
                received_data += data.decode() + "\n"
                # print("Received:", data.decode())
            else:
                received_data = ""
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        conn.close()
        print(f"Connection with {addr} closed.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return jsonify({'data': received_data})

if __name__ == "__main__":
    Thread(target=start_socket_server).start()
    app.run(debug=True, host='0.0.0.0', port=5000)

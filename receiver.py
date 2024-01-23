import socket

def start_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)
    print(f"Listening on {host}:{port}")

    # Accept a new connection
    conn, addr = server.accept()
    print(f"Connected to {addr}")

    try:
        while True:
            data = conn.recv(1024)
            if data:
                print("Received:", data.decode())

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        conn.close()
        print(f"Connection with {addr} closed.")

if __name__ == "__main__":
    HOST = '0.0.0.0'  # Listening on all interfaces
    PORT = 12345      # Port to listen on (non-privileged ports are > 1023)
    start_server(HOST, PORT)

import socket
import threading

def client_handler(conn, addr):
    print(f"Connection established with {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"From {addr}: {data.decode()}")
        conn.sendall(data)
    conn.close()
    print(f"Connection closed with {addr}")

def launch_server():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.bind(('localhost', 12345))
    srv.listen()
    print("Server is running on port 12345")

    while True:
        conn, addr = srv.accept()
        threading.Thread(target=client_handler, args=(conn, addr)).start()

def launch_client():
    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli.connect(('localhost', 12345))
    print("You are connected to the server")

    try:
        while True:
            msg = input("Type your message: ")
            cli.sendall(msg.encode())
            response = cli.recv(1024).decode()
            print("Echoed back:", response)
    except KeyboardInterrupt:
        print("Exiting client...")
    finally:
        cli.close()

if __name__ == "__main__":  # Correct condition
    server_thread = threading.Thread(target=launch_server)
    server_thread.start()

    launch_client()

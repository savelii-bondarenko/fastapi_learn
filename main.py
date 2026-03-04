import socket
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

HOST = '127.0.0.1'
PORT = 8080

def server_start():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    logger.info(f"Listening on http://{HOST}:{PORT}")
    while True:
        client_socket, address = server_socket.accept()
        logger.info(f"User from {address}")

        request_data = client_socket.recv(4096).decode("utf-8")
        logger.info(f"Received {request_data}")

        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            "Content-Length: 20\r\n"
            "Connection: close\r\n"
            "\r\n"
            "<h1>Hello World!</h1>"
        )

        client_socket.sendall(response.encode("utf-8"))
        client_socket.close()

if __name__ == "__main__":
    server_start()

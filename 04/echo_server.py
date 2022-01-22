import sys
import socket


BUF_SIZE = 1024


def main(port):
    print('port', port)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    server.bind(('localhost', int(port)))
    server.listen(5)

    
    while True:
        (clnt_socket, clnt_addr) = server.accept()
        msg = clnt_socket.recv(BUF_SIZE)
        print(f'msg from clnt ... : {msg}')

        clnt_socket.sendall((msg + b' from server'))
        clnt_socket.close()

    server.close()


if __name__ == '__main__':
    port = sys.argv[1]
    main(port)

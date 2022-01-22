import sys
import socket


def main(ip, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    

    while True:
        client.connect((ip, int(port)))

        msg = input('< input >>')

        l = client.send(msg.encode())
        print('l --', l)
        server_msg = b''
        while True:
            packet = client.recv(1024)
            if packet == b'':
                break
            server_msg += packet
            print(server_msg)



if __name__ == '__main__':
    ip, port = sys.argv[1:3]
    main(ip, port)

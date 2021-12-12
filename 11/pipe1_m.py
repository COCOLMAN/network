from multiprocessing import Pipe
import os


def main():
    text = "Who are you?"

    a, b = Pipe()

    pid = os.fork()
    if pid == 0:
        a.send(text)
    else:
        data = b.recv()
        print(data)



if __name__ == '__main__':
    main()

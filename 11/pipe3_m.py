import os
from multiprocessing import Pipe


def main():
    text1 = 'Who are you?'
    text2 = 'Thank you for your message'

    a, b = Pipe()

    pid = os.fork()
    if pid == 0:
        a.send(text1)
        data = a.recv()
        print('Child proc output -', data)
    else:
        data = b.recv()
        print('Parent proc output -', data)
        b.send(text2)



if __name__ == '__main__':
    main()

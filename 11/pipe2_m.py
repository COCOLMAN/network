import time
import os
from multiprocessing import Pipe


def main():
    text1 = 'Who are you?'
    text2 = 'Thank you for your message'

    a, b = Pipe()

    pid = os.fork()
    if pid == 0:
        a.send(text1)
        time.sleep(2)
        data = b.recv()
        print('Child proc output -', data)
    else:
        data = b.recv()
        print('Parent proc output -', data)
        a.send(text2)
        time.sleep(3)




if __name__ == '__main__':
    main()

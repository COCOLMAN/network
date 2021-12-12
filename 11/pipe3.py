import time
import os


def main():
    text1 = b'Who are you?'
    text2 = b'Thank you for your message'

    r1, w1 = os.pipe()
    r2, w2 = os.pipe()

    pid = os.fork()
    if pid == 0:
        os.write(w1, text1)
        data = os.read(r2, 30)
        print('Child proc output -', data)
    else:
        data = os.read(r1, 30)
        print('Parent proc output -', data)

        os.write(w2, text2)




if __name__ == '__main__':
    main()

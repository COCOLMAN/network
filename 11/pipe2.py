import time
import os


def main():
    text1 = b'Who are you?'
    text2 = b'Thank you for your message'

    r, w = os.pipe()

    pid = os.fork()
    if pid == 0:
        os.write(w, text1)
        time.sleep(2)
        data = os.read(r, 30)
        print('Child proc output -', data)
    else:
        data = os.read(r, 30)
        print('Parent proc output -', data)

        os.write(w, text2)
        time.sleep(3)




if __name__ == '__main__':
    main()

import os


def main():
    text = b'Who are you?'

    r, w = os.pipe()

    pid = os.fork()
    if pid == 0:
        os.write(w, text)
    else:
        data = os.read(r, 30)
        print(data)

if __name__ == '__main__':
    main()

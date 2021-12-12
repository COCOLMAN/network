import os
import time


def main():
    pid = os.fork()

    if pid == 0:
        print('Hi, I am a child process')
    else:
        print(f'Child Process ID : {pid}')
        time.sleep(30)

    if pid == 0:
        print('End child process ')
    else:
        print('End Parent process')


if __name__ == '__main__':
    main()

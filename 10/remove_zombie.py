import time
import sys
import os
import signal


def read_childproc(sig, frame):
    print('call sig')
    pid, status = os.wait()
    if os.WIFEXITED(status):
        print('Remove proc id : ', pid)
        print('Child send ', os.WEXITSTATUS(status))


def main():
    signal.signal(signal.SIGCHLD, read_childproc)
    pid = os.fork()

    if pid == 0:
        print("Hi! I'm child 1 process!")
        time.sleep(10)
        sys.exit(12)
    else:
        print('child proc id : ', pid)
        pid = os.fork()
        if pid == 0:
            print("Hi! I'm child 2 process!")
            time.sleep(10)
            sys.exit(24)
        else:
            print('Child proc id : ', pid)
            for _ in range(5):
                print("wait...")
                time.sleep(5)

if __name__ == '__main__':
    main()

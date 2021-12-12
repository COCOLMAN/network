import signal


def timeout(sig, frame):
    print(sig, frame)
    if sig == signal.SIGALRM:
        print('Time out!')
    signal.alarm(2)


def keycontrol(sig, frame):
    if sig == signal.SIGINT:
        print('CTRL + c pressed')


def main():
    signal.signal(signal.SIGALRM, timeout)
    signal.signal(signal.SIGINT, keycontrol)
    signal.alarm(2)

    for _ in range(2):
        print('wait ...')
        signal.pause()


if __name__ == '__main__':
    main()

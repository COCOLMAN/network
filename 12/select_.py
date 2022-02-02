import sys
import select


def main():
    while True:
        a, b, c = select.select([sys.stdin], [], [], 5)
        if not any([a, b, c]):
            print("Time out !")
        else:
            for conn in a:
                r = conn.readline()
                print('message from console: ', r)
        


if __name__ == '__main__':
    main()

import os


gval = 10


def main():
    lval = 20
    global gval
    gval += 1
    lval += 5

    pid = os.fork()

    if pid == 0:
        gval += 2
        lval += 2
    else:
        gval -= 2
        lval -= 2

    if pid == 0:
        print(f'Child Proc: [{gval}, {lval}]')
    else:
        print(f'Parent Proc: [{gval}, {lval}]')


if __name__=='__main__':
    main()

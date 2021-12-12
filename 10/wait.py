import os
import sys



# use wait

def main1():
    print('use os.wait')

    pid = os.fork()

    if pid == 0:
        sys.exit(3)
    else:
        print(f'Child PID : {pid} \n')
        pid = os.fork()
        if pid == 0:
            sys.exit(7)
        else:
            print(f'Child PID : {pid} \n')

            pid, status = os.wait()
            if os.WIFEXITED(status):
                print('Child send one : ', os.WEXITSTATUS(status))

            pid, status = os.wait()
            if os.WIFEXITED(status):
                print('Child send two : ', os.WEXITSTATUS(status))


# use waitpid
def main2():
    print('use os.waitpid')

    pid1 = os.fork()

    if pid1 == 0:
        sys.exit(3)
    else:
        print(f'Child PID : {pid1} \n')
        pid2 = os.fork()
        if pid2 == 0:
            sys.exit(7)
        else:
            print(f'Child PID : {pid2} \n')

            pid, status = os.waitpid(pid1, 0)
            if os.WIFEXITED(status):
                print('Child send one : ', os.WEXITSTATUS(status))

            pid, status = os.waitpid(pid2, 0)
            if os.WIFEXITED(status):
                print('Child send two : ', os.WEXITSTATUS(status))





if __name__ == '__main__':
    main1()

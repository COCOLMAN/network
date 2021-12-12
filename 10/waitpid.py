import os
import time
import  sys


def main():
    pid = os.fork()
    if pid == 0:
        time.sleep(15)
        sys.exit(24)
    else:
        while True:
            try:
                pid, status = os.waitpid(-1, os.WNOHANG)
            except ChildProcessError:
                break
            time.sleep(3)
            print('sleep 3sec.')
        """
        os.waitpid(pid, option)

        pid 가 0보다 크면, waitpid()는 해당 프로세스에 대한 상태 정보를 요청합니다. 
        pid 가 0이면, 현재 프로세스의 프로세스 그룹에 있는 모든 자식의 상태를 요청합니다. 
        pid 가 -1이면, 현재 프로세스의 모든 자식의 상태를 요청합니다. 
        pid 가 -1보다 작으면, 프로세스 그룹 -pid(pid 의 절댓값)에 있는 모든 프로세스의 상태를 요청합니다.
        """

        if (os.WIFEXITED(status)):
            print('Child send ', os.WEXITSTATUS(status))
        


if __name__ == '__main__':
    main()
    

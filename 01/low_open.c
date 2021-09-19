#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

void error_handling(char* message);

int main(void){
  int fd, fd2;
  char buf[]="Let's go!\n";

  fd=open("data.txt", O_CREAT|O_WRONLY|O_TRUNC);
  if (fd == -1) {
    error_handling("open() error!");
  }
  printf("file descriptor: %d\n", fd);

  fd2=open("data2.txt", O_CREAT|O_WRONLY|O_TRUNC);
  if (fd2 == -1) {
    error_handling("open() 2 error!");
  }
  printf("file descriptor: %d\n", fd2);

  if(write(fd, buf, sizeof(buf))==-1){
    error_handling("write() error!");
  }
  close(fd);
  close(fd2);
  return 0;
}

void error_handling(char *message){
  fputs(message, stderr);
  fputs("\n", stderr);
  exit(1);
}

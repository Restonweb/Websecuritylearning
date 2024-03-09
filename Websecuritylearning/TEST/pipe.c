#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<fcntl.h>
#include<unistd.h>
int main(){
    int pid1,pid2;
    int fd[2];
    char out[512],in[512];
    pipe(fd);
    pid1=fork();
    if(pid1==0){
        sprintf(out,"%d is sending a message to parent!\n",getpid());
        printf("%s",out);
        write(fd[1],out,sizeof(out));
    }else{
        read(fd[0],in,sizeof(out));
        printf("%s",in);
    }
    return 0;
}
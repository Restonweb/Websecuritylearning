#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int main(){
    pid_t child_pid;
    child_pid = fork();

    if(child_pid == 0){
        int i = 0;
        for(;i<5;i++)
        {
            printf("child\n");
            sleep(1);
        }
    }else{
        printf("child's pid is %d\n,child_pid");
    }
    int j = 0;
    for(;j<5;j++){
        printf("parent\n");
        sleep(1);
    }
    return 0;
}
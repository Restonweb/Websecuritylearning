#include <stdio.h>
#include <unistd.h>

int main(){
    pid_t pid_son,pid_daughter;

    pid_son = fork();
    if(pid_son == 0){
        printf("I'm son");
    }else{
        printf("I'm Farther");

        pid_daughter = fork();

        if(pid_daughter == 0){
            printf("I'm daughter");
        }else{
            printf("I'm Farther");
        }
    }
    return 0;
}
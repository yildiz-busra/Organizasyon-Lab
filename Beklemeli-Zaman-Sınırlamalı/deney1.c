#include <stdio.h>
#include <time.h>
#include <sys/time.h>

#define N 1000
int main(){
    struct timeval t_before, t_after, t_diff;
    gettimeofday(&t_before, NULL);

    float A[N][N], B[N][N];
    for(int i=0;i<N;i++){
        for(int j=0;j<N;j++){
            A[i][j] = A[i][j] + B[i][j];
        }
    }
    gettimeofday(&t_after, NULL);
    timersub(&t_after, &t_before, &t_diff);
    printf("%ld.%0.6ld s\n", (long int)t_diff.tv_sec, (long int)t_diff.tv_usec);
}
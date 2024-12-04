#include <stdio.h>
#include <time.h>
#include <sys/time.h>

#define N 10000
#define blok_boyu 20
int main(){
    struct timeval t_before, t_after, t_diff;
    gettimeofday(&t_before, NULL);

    float A[N][N], B[N][N];
    for(int i=0;i<N;i+=blok_boyu){
        for(int j=0;j<N;j+=blok_boyu){
            for(int ii=i;ii<i+blok_boyu;ii++){
                for(int jj=j;jj<j+blok_boyu;jj++){
                    A[ii][jj] = A[ii][jj] + B[jj][ii];
                }
            }
        }
    }
    gettimeofday(&t_after, NULL);
    timersub(&t_after, &t_before, &t_diff);
    printf("%ld.%0.6ld s\n", (long int)t_diff.tv_sec, (long int)t_diff.tv_usec);
}
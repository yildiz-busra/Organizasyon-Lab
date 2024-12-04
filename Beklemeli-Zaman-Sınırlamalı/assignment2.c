#include <immintrin.h>
#include <stdio.h>
#include <time.h>
#include <sys/time.h>

#define N 1000

int main() {

    struct timeval t_before, t_after, t_diff;
    gettimeofday(&t_before, NULL);

    double veca[N];
    double vecb[N];
    double vecc[N];

    for (int i=0;i<N;i++){
        veca[i]=6.0;
        vecb[i]=2.0;
        vecc[i]=7.0;
    }

    for (int i = 0; i < N; i++) {
        if (i % 2 == 0) {
            vecc[i] = veca[i] * vecb[i] - vecc[i];
        } else {
            vecc[i] = veca[i] * vecb[i] + vecc[i];
        }
    }

    gettimeofday(&t_after, NULL);
    timersub(&t_after, &t_before, &t_diff);
    printf("%ld.%0.6ld s\n", (long int)t_diff.tv_sec, (long int)t_diff.tv_usec);

    return 0;
}
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
    double result[N];

    for (int i=0;i<N;i++){
        veca[i]=6.0;
        vecb[i]=2.0;
        vecc[i]=7.0;
    }
    for (int i=0;i<N;i++){
        __m256d vecA = _mm256_loadu_pd(&veca[i]);
        __m256d vecB = _mm256_loadu_pd(&vecb[i]);
        __m256d vecC = _mm256_loadu_pd(&vecc[i]);

        __m256d resv = _mm256_fmaddsub_pd(vecA, vecB, vecC);
        _mm256_storeu_pd(&result[i], resv);
    }


    gettimeofday(&t_after, NULL);
    timersub(&t_after, &t_before, &t_diff);
    printf("%ld.%0.6ld s\n", (long int)t_diff.tv_sec, (long int)t_diff.tv_usec);

    return 0;
}
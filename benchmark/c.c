// MKY assigment 3 benchmark

#include <stdio.h>
#include <stdint.h>

int main(int argc, uint8_t** argv)
{
    uint64_t a = 12354;
    uint64_t b = 52529;
    int i = 0;

    for (i = 0; i < 100000000; ++i)
    {
        a = (a * b) % 1000000;
    }
    printf("%d\n", a);


    return 0;
}

/**
 * MI-MKY ukol 3
 * Tomas Susanka
 **/

#include <stdio.h>
#include <math.h>
#include "functions.c"

#define DEBUG 0


int main(int argc, char** argv)
{
	int mod = 113;
	int o = 112; // order
	int g = 3;
	int h = 57;  // looking for (3^? = 57 mod 113) which is (log3 57 = ? mod 113)

	int n = (int) ceil(sqrt(mod)); // n = 11
	int arrayA[n];
	int arrayB[n];

	printf("p = %d\n", mod);
	printf("o = %d\n", o);
	printf("g = %d\n", g);
	printf("h = %d\n", h);
	printf("n = %d\n", n);


	arrayA[0] = 1;
	arrayA[1] = g;
	printf("FILLING ARRAY\n");
	printf("i=0: 1\n");
	printf("i=1: %d\n", arrayA[1]);
	for (int i = 2; i < n; ++i)
	{
		arrayA[i] = mult(arrayA[i-1], g, mod);
		printf("i=%d: %d\n", i, arrayA[i]);
	}

	return 0;
}

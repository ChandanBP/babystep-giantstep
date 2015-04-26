/**
 * MI-MKY ukol 3
 * Tomas Susanka
 **/

#include <stdio.h>
#include <math.h>
#include <algorithm>
#include "functions.c"
#include "vector.c"

#define DEBUG 0

int main(int argc, char** argv)
{

	vector<int> x(5);
	x[0] = 0;
	x[1] = 11;
	x[2] = 2;
	x[3] = 8;
	x[4] = 5;

	sort_indexes(x);
	for (auto i: sort_indexes(x))
	{
		printf("%d\n",i);
	}
	return 2;


	int mod = 113;
	int order = 112; // order
	int g = 3;
	int h = 57;  // looking for (3^? = 57 mod 113) which is (log3 57 = ? mod 113)

	int n = (int) ceil(sqrt(mod)); // n = 11
	int arrayA[n];
	int arrayB[n];

	arrayA[0] = 1;
	for (int i = 1; i < n; ++i)
	{
		arrayA[i] = mult(arrayA[i-1], g, mod);
	}



	// todo: throw away all previous results
	int tmp = inverse(g, mod, order);
	tmp = power(tmp, n, mod); // 58
	arrayB[0] = h;
	for (int i = 1; i < n; ++i)
	{
		arrayB[i] = mult(arrayB[i-1], tmp, mod);
	}


	return 0;
}

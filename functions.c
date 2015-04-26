/**
 * MI-MKY ukol 3
 * Tomas Susanka
 **/

#include <stdio.h>
#include <stdint.h>

#define DEBUG_F 0

int mult(int a, int b, int mod)
{
	a = a * b;
	return a % mod;
}

int square(int a, int mod)
{
	int b = a * a;
	return b % mod;
}

/**
 * Finds inverse of @num in @mod in group of order @order
 */ 
int inverse(int num, int mod, int order)
{
	int power = order - 1;
	int max = 2147483648; // 2^31

	int last = 1;

	int i = 0;
	int start = 0;

	for (i = (sizeof(int) * 8) - 1; i > 0; i--)
	{
		power = power << 1;
		if (start == 0 && (power & max))
		{
			start = 1;
		}
		if (start)
		{
			if (DEBUG_F) printf("counting %llu ^ 2 mod %llu: ", last, mod);
			last = square(last, mod);
			if (DEBUG_F) printf("%llu\n", last);
			if (power & max)
			{
				if (DEBUG_F) printf("counting %llu * %llu mod %llu: ", last, num, mod);
				last = (last * num) % mod;
				if (DEBUG_F) printf("%llu\n", last);
			}
		}
	}

	return last;
}

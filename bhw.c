/**
 * MI-BHW ukol 4
 * gf(2^m) AVR projective
 *
 * Tomas Susanka & Peter Poljak
 *
 **/

 /**
  * We're using polynomial base to represent f, eg: (101001) = x^5 + x^3 + 1
  *
  */

#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <assert.h>
#include <stdbool.h>

#define DEBUG 1

#define ARRAY_LENGTH 5

#define ONE_NOT_FOUND 9

uint8_t pattern[8] = {0x80,0x40,0x20,0x10,0x08,0x04,0x02,0x01};


void printBin(uint8_t x)
{
	int i = 0;
	for (i = sizeof(uint8_t) * 8 - 1; i >= 0; i--)
	{
		(x & (1<<i)) ? putchar('1') : putchar('0');
	}

	printf(" ");
}

void printBinWhole(uint8_t* array, int length)
{
	int i = 0;
	for (i = 0; i < length; ++i)
	{
		printBin(array[i]);
	}
    printf("\n");
}

void printHexWhole(uint8_t* array, int length)
{
    int i = 0;
    for (i = 0; i < length; ++i)
    {
        printf("%02x", array[i]);
    }
	printf("\n");
}

/**
 * Sets all elements of array to 0
 */
void zeroArray(uint8_t* array, int length)
{
	int i = 0;
	for (i = 0; i < length; ++i)
	{
		array[i] = 0;
	}
}

/**
 * Reads input from stdin
 */
uint8_t loadInput(uint8_t* a, uint8_t* b)
{
    zeroArray(a,ARRAY_LENGTH);
    zeroArray(b,ARRAY_LENGTH);
    int res = 0;

    printf("Enter a:");
    res += scanf("%2x%2x%2x%2x%2x", &a[0], &a[1], &a[2], &a[3], &a[4]);
    printf("\nEnter b:");
    res += scanf("%2x%2x%2x%2x%2x", &b[0], &b[1], &b[2], &b[3], &b[4]);
    printf("\n");

    return res;
}

/**
 * Adds a + b and stores output in result
 **/
void add(uint8_t* a, uint8_t* b, uint8_t* result)
{
    int i = 0;
    for (i = 0; i < ARRAY_LENGTH; i++)
    {
        result[i] = a[i] ^ b[i];
    }
}

/**
 * Linear feedback shift register implements A=Ax
 **/
void lfsr(uint8_t* number)
{
    uint8_t x33, i, x34, x32, tmp = 0x00;

    x34 = number[0] & pattern[5];
    x32 = number[0] & pattern[7];
    x34 >>= 2;
    x33 = x34 ^ x32;
    x33 <<= 1;

    for(i = 0; i < ARRAY_LENGTH; i++)
    {
        if ((number[i] > 0x00) && (i > 0))
        {
            if ((0x80 & number[i]) > 0x00) number[i-1] += pattern[7];
        }
        number[i] = number[i] << 1;
    }
    tmp = number[0] & ~pattern[6]; // destroys 6. bit
	number[0] = tmp | x33;

	// x34 is shifted to x^0
	// no need for destroying here because the bit is always 0 due to the shift
    number[4] = number[4] | x34;

	// 1. bit ever needs to be destroyed, the shift could move 1 in here
    number[0] = number[0] & ~pattern[4];
}

/**
 * Multiplies a * b and stores it in result.
 **/
void mult(uint8_t* a, uint8_t* b, uint8_t* result)
{
    // TODO: check number validity (first nibble must be zero)

    uint8_t tmp = 128; // 2^7
    int i, j  = 0;

    for(i = 0; i < ARRAY_LENGTH; i++) 
    {
        for (j = 0; j < 8; j++)
        {
            if ((i == 0) && (j == 0))
            {
                j = 3;
                tmp = tmp >> 4; // can be left out?
                continue;
            }
            if (b[i] & tmp)
            {
                add(result, a, result);
            }
            if ((i == ARRAY_LENGTH - 1) && (j == 7))
        	{
        		result[0] = result[0] & ~pattern[4]; // destroys 1 bit.
        		break;
        	}
            lfsr(result);

            tmp = tmp >> 1;
        }
        tmp = 128;
    }
}

/*****************************************************************************************************************************/
/*****************************************************************************************************************************/

int main(int argc, uint8_t** argv)
{
	uint8_t temp[ARRAY_LENGTH];
    uint8_t result[ARRAY_LENGTH];
    zeroArray(result, ARRAY_LENGTH);

    uint8_t a[ARRAY_LENGTH];
    uint8_t b[ARRAY_LENGTH];

    uint8_t inverse[ARRAY_LENGTH] = {0x05, 0x00, 0x00, 0x00, 0x00};

    loadInput(a, b);

    printf("a = ");
    printHexWhole(a, ARRAY_LENGTH);
    printf("b = ");
    printHexWhole(inverse, ARRAY_LENGTH);

    mult(a, inverse, result);
    printHexWhole(result, ARRAY_LENGTH);

	return 0;
}

#include <stdio.h>
#include <string.h>
#include <math.h>

int main()
{
	int length, i=0;
	char seq [3000];
 	scanf("%s", seq);
	length = strlen (seq);
	for ( i=0 ; i<length ; i++)
	{
		if (seq [i] == 'D' || seq [i] == 'E' || seq [i] == 'H' || seq [i] == 'K' || seq [i] == 'N' || seq [i] == 'Q' || seq [i] == 'R')
			printf(" ");
		else if (seq [i] == 'S' || seq [i] == 'T' || seq [i] == 'G')
			printf(".");
		else if (seq [i] == 'A' || seq [i] == 'C' || seq [i] == 'M' || seq [i] == 'P')
			printf(":");
		else if (seq [i] == 'F' || seq [i] == 'I' || seq [i] == 'L' || seq [i] == 'V'|| seq [i] == 'W' || seq [i] == 'Y' ) 
			printf("*");
	}

}


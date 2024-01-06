#include <stdio.h>
#include <string.h>
#include <math.h>

int main()
{
	char seq[1000];
	int length, i=0;
 	
	for (i=0;i<=10;i++ )
	{
		scanf("%s", seq);
		length = strlen(seq); 
		printf("The length is %d \n",length);

	}
}

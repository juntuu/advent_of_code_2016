#include <stdio.h>

int main(void)
{
	int i = 0;
	while (i < 7 * 365)
		i = i << 2 | 0b10;
	printf("%d\n", i - 7 * 365);
}

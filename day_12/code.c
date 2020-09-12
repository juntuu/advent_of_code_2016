#include <stdio.h>

typedef int T;

T run(T c)
{
	T a, b, d;
	a = 1;
	b = 1;
	d = 26;
	if (c != 0)
		d += 7;
	do {
		c = a;
		a += b;
		b = c;
		--d;
	} while (d != 0);
	return a + 19 * 14;
}

int main()
{
	printf("A=%d\n", run(0));
	printf("B=%d\n", run(1));
}

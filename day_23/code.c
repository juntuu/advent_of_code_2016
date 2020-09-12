#include <stdio.h>

typedef int T;

T run(T a)
{
	T b = a;
	while (--b)
		a *= b;
	return a + 70 * 78;
}

int main()
{
	fprintf(stderr, "A=%d\n", run(7));
	fprintf(stderr, "B=%d\n", run(12));
}

#include <stdio.h>
int main() {
	int n, i, sum;
	sum = 0;
	scanf("%d", &n);

	for (i = 0; i <= (n - 1); i++) {
		sum = sum + (1 + 2 * i ) * ( 2 * ( n - 1 ) + 1 - 2 * i);
	}
	printf("%d", sum);
	scanf("%d", &n);
}
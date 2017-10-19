#include <stdio.h>
int main() {
	int n, i, nb_measure;
	nb_measure = 0;

	scanf_s("%d", &n, 30000);
	
	for (i = 1; i <= n; i++) {
		if (n % i == 0) {
			nb_measure++;
		}
	}
	if (nb_measure == 2) {
		printf("prime");
	}
	else {
		printf("not prime");
	}
	scanf_s("%d", &n, 30000);
}
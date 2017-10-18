#include <stdio.h>
int main() {
	int i,n, nb_measure;
	nb_measure = 0;
	scanf("%d", &n);
	for (i = 1; i <= 10000; i++) {
		if (n % i == 0) {
			nb_measure++;
		}
	}
	if (2 * nb_measure + 1 % 2 == 1) {
		printf("yes");
	}
	else {
		printf("no");
	}

	return 0;
}
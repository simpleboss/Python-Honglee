#include <stdio.h>
int main() {
	int i,n, nb_measure;
	nb_measure = 0;
	scanf("%d", &n);

	for (i = 1; i <= n; i++) {
		if (n % i == 0) {
			nb_measure++;
		}
	}
//	printf("nb_measure = %d\n", nb_measure);

	if ( nb_measure  % 2 == 1) {
		printf("yes");
	}
	else {
		printf("no");
	}
	scanf("%d", &i);
	return 0;
}
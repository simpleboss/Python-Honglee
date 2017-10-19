#include <stdio.h>
int main() {
	int first, second, temp, i, nb_measure;
	nb_measure = 0;

	scanf("%d %d", &first, &second);
	
	if (first > second) {
		temp = first;
		first = second;
		second = first;
	}
	for (i = 1; i <= first; i++) {
		if (first % i == 0 && second % i == 0) {
			nb_measure++;
		}
	}
	if (nb_measure == 1) {
		printf("yes");
	}
	else {
		printf("no");
	}
	scanf("%d", &first);
}
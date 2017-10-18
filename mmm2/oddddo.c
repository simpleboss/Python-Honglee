#include <stdio.h>
int main() {
	int first, second, i, max,min;
	scanf("%d %d", &first, &second);

	for (i = 2; ; i++) {
		if (i / first == i / second){
			min == i;
			break;
		if (i <= 1000 && first % i == 0 && second % i == 0) {
			max == i;
		}
	}
		return 0;
}
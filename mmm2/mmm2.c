#include <stdio.h>
#include <math.h>
int main() {
	int i, n, max, min, cost, hill;
	max = 0;
	min = 1000;

	scanf("%d", &n);
	for (i = 1; i <= n; i++) {
		scanf("%d", &hill);
		if (max < hill) {
			max = hill;
		}
		else if (min > hill) {
			min = hill;
		}
	}
//	printf("max = %d\n", max);
//	printf("min = %d\n", min);

//	printf("max - min = %d\n", max - min);

	cost = 2 * (int)pow((max - min - 17.0) / 2, 2.0);
	printf("%d", cost);

	scanf("%d", &i);
	return 0;

}
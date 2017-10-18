#include <stdio.h>
int main(){
	int first, second, i, max, min, temp;
	scanf("%d %d", &first, &second);
	if (first > second) {
		temp = first;
		first = second;
		second = temp;
	}
	for (i = 1; i<=1000 ; i++) {
		if (first % i == 0 && second % i == 0) {
			max = i;
		}
				
	}
	for (i = 1; i <= 1000; i++) {
		if (first * i % second == 0) {
			min = first * i;
			break;
		}
	}
	printf("%d %d", max, min);
	scanf("%d", &i);
	return 0;
}
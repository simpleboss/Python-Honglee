#include <stdio.h>
int main(){
	int first, second, i, max, min, temp;
	scanf("%d %d", &first, &second);
	if (first > second) {
		temp = first;
		first = second;
		second = temp;
	}
	for (i = 1; ; i++) {
		if (i <= 1000 && first % i == 0 && second % i == 0) {
			max = i;
		}
		if ( first * i % second == 0 ) {
			min = i;
			break;
		}
		
	}
	printf("%d %d", min, max);
	scanf("%d", &i);
	return 0;
}
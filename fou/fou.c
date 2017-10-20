#include <stdio.h>

int main() {
	int first, second, third, temp, d1, d2;
	scanf_s("%d %d %d", &first, &second, &third);

	if (first > second) {
		temp = first;
		first = second;
		second = temp;
	}

	if (first > third) {
		temp = first;
		first = third;
		third = temp;
	}

	if (second > third) {
		temp = second;
		second = third;
		third = temp;
	}

	//printf("first second third = %d %d %d \n", first, second, third);
	d1 = second - first;
	d2 = third - second;

	if (d1 == d2) {
		printf("%d", third + d1);
	}
	else if (d1 > d2) {
		printf("%d", first + d2);
	}
	else {
		printf("%d", second + d1);
	}
	scanf_s("%d %d %d", &first, &second, &third);

	return 0;
}
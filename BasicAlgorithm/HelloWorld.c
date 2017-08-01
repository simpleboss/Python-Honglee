#include <stdio.h>
int main()
{
	int int1, int2, int3, temp;
	scanf("%d %d %d", &int1, &int2, &int3);

	if (int1 > int2) {
		temp = int2;
		int2 = int1;
		int1 = temp;
	}
	if (int1 > int3) {
		temp = int3;
		int3 = int1;
		int1 = temp;
	}
	if (int2 > int3) {
		temp = int3;
		int3 = int2;
		int2 = temp;
	}

	if (pow(int1, 2.0) + pow(int2, 2.0) == pow(int3, 2.0)) {
		printf("right");
	}
	else if (pow(int1, 2.0) + pow(int2, 2.0) > pow(int3, 2.0)){
		printf("acute");
	}
	else if (pow(int1, 2.0) + pow(int2, 2.0) < pow(int3, 2.0) {
		printf("obtuse");
	}

	return 0;

}
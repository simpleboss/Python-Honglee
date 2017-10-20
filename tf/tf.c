#include <stdio.h>
#include <math.h>
int main() {
	int n, r, l, l_answer, r_answer;

	scanf_s("%d", &n, 1000000);
	//printf("scanf_s complete\n");
	//printf("(int)pow(2.0, (double)0) = %d\n", (int)pow(2.0, 0.0));
	for (l_answer = 1; l_answer <= n; l_answer = l_answer + 2) {
		
		for (r_answer = 0; r_answer <= 20; r_answer++) {
			//printf("start for r_answer");
			r = (int)pow(2.0, (double)r_answer);
			if (n == l_answer * r) {
				//printf("yes");
				printf("%d %d\n", l_answer, r_answer);
				break;
			}
		}
	}
	scanf_s("%d", &n,1000000);
	return 0;
}
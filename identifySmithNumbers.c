#include <stdio.h>
/*
	Challenge Link: https://www.hackerrank.com/challenges/identify-smith-numbers
*/
int divide(number){
	int sum = 0;
	while(number){
		sum += number%10;
		number /= 10;
	}
	return sum;
}
int checkPrimeSum(int number){
	int divisor = 2,sum =0,toAdd;
	while (number>1) {
		if(number % divisor == 0){
			int i = 0;
			while(number % divisor == 0){
				toAdd = divide(divisor);
				sum += toAdd;
				number /= divisor;
			}	
		}
		divisor += 1;
	}
	//printf("%d\n",sum);
	return sum;
}
int checkSum(int number){
	int sumNum=0;
	while(number){
		sumNum += number%10;
		number = number / 10;
		
	}
	//printf("%d\n",sumNum);
	return sumNum;
}
int checkSmith(int number){

	int	sumPrime=0,
		sumNum=0;
	sumNum = checkSum(number);
	//printf("%d\n",sumNum);
	sumPrime = checkPrimeSum(number);
	//printf("%d\n",sumPrime);
	if(sumNum == sumPrime) return 1;
	return 0;
}


int main() {
	int number,isSmith;
	scanf("%d",&number);
	isSmith = checkSmith(number);
	printf("%d",isSmith);
	//system("Pause");
	return 0;
}


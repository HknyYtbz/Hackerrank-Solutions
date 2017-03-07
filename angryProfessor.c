#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
 /*  
	Challenge Link: https://www.hackerrank.com/challenges/angry-professor
 */
int main() {
    int testcase,i,j;
    int need,student;
    int *students;
    scanf("%d",&testcase);
    for(i=0;i<testcase;i++){
        int counter=0;
        scanf("%d %d",&student,&need);
        students = (int*) malloc(sizeof(int)*student);
        for(j = 0;j<student;j++){
            scanf("%d",&students[j]);
        }
        for(j=0;j<student;j++){
            if(students[j]<=0) counter +=1;
        }
        if(counter >= need) printf("NO\n");
        else                printf("YES\n");
    }
       
    return 0;
}

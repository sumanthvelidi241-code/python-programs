num = input("Enter Number: ")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)

"""
#include<stdio.h>

int main ()
{
    int num, sum = 0;
 
    num = 1234;
    printf("The number is = %d\n",num);
    while(num!=0){
        sum += num % 10;
        num = num / 10;
    }
    printf("Sum: %d\n",sum);
    return 0;
}
"""
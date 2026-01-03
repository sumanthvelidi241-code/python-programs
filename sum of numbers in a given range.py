num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = 0
for i in range(num1,num2+1):
  sum+=i
print(sum)

"""
#include <stdio.h>

int main()
{
    int a = 5;
    int b = 10;
    int sum = 0;
    for (int i = a; i <= b; i++)
        sum = sum + i;
    printf("%d",sum);
    return 0;
}
"""
num = int(input("Enter Number: "))
temp = num
reverse = 0
while num > 0:
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    num = num // 10

print(reverse)

"""
#include<stdio.h>

//main program
int main ()
{
  int num, reverse = 0, rem;
  num=1234;
  printf("The number is: %d\n",num);
    while(num != 0)
    {
      rem = num % 10;
      reverse = reverse * 10 + rem;
      num /= 10;
    };
  printf("Reverse: %d\n",reverse); 
  return 0;
}
"""
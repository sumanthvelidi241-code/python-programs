num = int(input("Enter Number: "))
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")

"""
#include<stdio.h> 
int main ()
{
    int num, reverse = 0, rem, temp;
    num=11211;
    printf("The number is :%d\n",num);
    temp = num;
    while(temp != 0)
    {
        rem = temp % 10;
        reverse = reverse * 10 + rem;
        temp /= 10;
    };
    if (num == reverse)
        printf("%d is Palindrome\n", num);
    else
        printf("%d is Not Palindrome\n", num);
}
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))   
max = 0
if num1 >= num2 and num1 >= num3:
  print(num1)
elif num2 >= num1 and num2 >= num3:
  print(num2)
else:
  print(num3)

"""
#include <stdio.h> 
int main ()
{
    int num1, num2, num3;   
    num1=12,num2=17,num3=19;
    if (num1 >= num2 && num1 >= num3)
        printf("%d is the greatest", num1);      
    else if(num2 >= num1 && num2 >= num3)
         printf("%d is the greatest", num2);
    else if(num3 >= num1 && num3 >= num2)
         printf("%d is the greatest", num3); 
    return 0;
}
"""
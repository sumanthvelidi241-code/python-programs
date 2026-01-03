number = int(input("Enter a number: "))
sum = 0
for i in range(number+1):
  sum+=i
print(sum)

"""
#include <stdio.h>
int main() 
{ 
    int Number, i, Sum = 0;
    printf ("\n Kindly Insert an Integer Variable\n");
    scanf ("%d", &Number);
    for(i = 1; i <= Number; i++)
    {
         Sum = Sum + i;
    }
    printf ("Sum of Natural Numbers = %d", Sum);
    return 0;
}
"""
year = int(input("Enter Year: "))

if (year%400 == 0) or (year%4==0 and year%100!=0):
    print("Leap Year")
else:
    print("Not a Leap Year")

"""
#include <stdio.h>
int main ()
{
    int year;
    year=2000;
    if(year % 400 == 0)
        printf("%d is a Leap Year",year); 
    else if(year % 4 == 0  && year % 100 != 0)
        printf("%d is a Leap Year",year);
    else
        printf("%d is not a Leap Year",year);
    return 0;
}
"""
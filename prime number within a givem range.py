low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))
primes = []

for i in range(low, high + 1):
    flag = 0

    if i < 2:
        continue
    if i == 2:
        primes.append(2)
        continue

    for x in range(2, i):
        if i % x == 0:
            flag = 1
            break

    if flag == 0:
        primes.append(i)
        
print(primes)
"""
#include <stdio.h>

int checkPrime(int num)
{
    if(num < 2){
        return 0;
    }
    else{   
        int x = num/2;
        for(int i = 2; i < x; i++)
        {
            if(num % i == 0)
            {
                return 0;
            }
        }
    }
    return 1;
}
int main()
{
    int a=10, b=20;
    for(int i=a; i <= b; i++){
        if(checkPrime(i))
            printf("%d ",i);
    }
    return 0;
}
"""
num = int(input("Enter a number: "))
flag = 0
for i in range(2,num):
  if num%i==0:
    flag = 1
    break
if flag == 1:
  print('Not Prime')
else:
  print("Prime")
"""
int main()
{
    int i, count = 0;
    int num = 19;
    for(i = 1; i <= num; i++) {
      if(num % i == 0) 
        count += 1;
    } 
       if(num == 0 || num == 1)
         printf("%d is not prime", num); 
       else if(count > 2) 
          printf("%d is not prime", num);
       else
         printf("%d is prime", num);
  return 0;
}
"""
num=int(input("Enter the Number:")) 
temp=num
sum=0
unit=0
while (num>0):
          unit=num%10 
          num=num//10
          sum=sum+(unit**3)
if (sum==temp):
          print("Number is Armstrong Number")
else:
          print("Number is Not Armstrong Number")
          
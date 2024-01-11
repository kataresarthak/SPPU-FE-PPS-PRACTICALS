list=[]
even=[]
odd=[]
n=int(input("Enter The Number of Values in the List:"))
for i in range(n):
    temp=int(input("Enter the Value:"))
    list.append(temp)
print("Entered List:",list)

for i in list:
    if (i%2==0):
        even.append(i)
    else:
        odd.append(i)
print("Even List:",even)
print("Odd List:",odd)

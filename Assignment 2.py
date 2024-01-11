EC=int(input("Enter the EC Marks: "))
EM1=int(input("Enter the EM1 Marks: "))
SME=int(input("Enter the SME Marks: "))
PPS=int(input("Enter the PPS Marks: "))
BEE=int(input("Enter the BEE Marks: "))
total=EC+EM1+SME+PPS+BEE
agg=total/5
grade="null"

if (EC>=40 and EM1>=40 and SME>=40 and PPS>=40 and BEE>=40):
              
              result="Pass"
              if (agg>=75):
                            grade="Distinction"
              elif(agg>=60 and agg<75):
                            grade="First class"
              elif(agg>=50 and agg<60):
                            grade="Second class"
              elif(agg>=40 and agg<50):
                            grade="Third class"
else:
              result="Fail"
print("Result:",result)
print("Total:",total)
print("Aggreget:",agg)
print("Grade:",grade)

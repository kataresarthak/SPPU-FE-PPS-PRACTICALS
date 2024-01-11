def menu():
    print("\n----------------MENU----------------\n\n 1.Calculate Length Of String\n 2.String Reversal\n 3.Equality Check of Two Strings\n 4.Check Palindrome\n 5.Check Substring\n 6.Exit\n")
    option=int(input("Enter Your Choice : "))
    return option

def reversal(str1):
    print("String Reversal :")
    for i in range(len(str1)-1,-1,-1):
        print(str1[i],end="")

def equality(str1,str2):
    if str1==str2:
        print("Stings are Equal",)
    else:
        print("Stings are Not Equal",)

def palindrome(str1):
    str2=""
    for i in range(len(str1)-1,-1,-1):
        str2+=str1[i]
    if str1 == str2:
        print("String is Palindrome")
    else:
        print("String is Not Palindrome")

def substring(str1,str2):
    if str2 in str1:
        print("Sting 2 is Substring of String 1",)
    else:
        print("Sting 2 is Not Substring of String 1",)

#Main program
option=menu()
if (option==1):
    str1=input("Enter the String 1 :  ")
    print("Length of String 1 : ", len(str1))
elif (option==2):
    str1=input("Enter the String 1  : ")
    reversal(str1)
elif (option==3):
    str1=input("Enter the String 1 : ")
    str2=input("Enter the String 2 : ")
    equality(str1,str2)
elif (option==4):
    str1=input("Enter the String 1 : ")
    palindrome(str1)
elif (option==5):
    str1=input("Enter the String 1 : ")
    str2=input("Enter the String 2 : ")
    substring(str1,str2)
elif (option==6):
    exit     
else:
    print("You have Entered Wrong Choice...!!")
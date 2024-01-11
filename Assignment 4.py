def sqrt(n):
              sqrt=n**0.5
              return sqrt
              
def sqr(n):
              return n*n

def cube(n):
              return n*n*n

def fact(n):
              fact=1
              for i in range(1,n+1):
                            fact=fact*i
              return fact

def prime(n):
              flag=0
              if n==1:
                            print("Number is Not prime")
              else:
                            for i in range(2,n):
                                          if(n%i==0):
                                                        flag=1
                                                        break
                            if (flag==1):
                                          print("Number is Not prime")
                            else:
                                          print("Number is prime")

def prime_fact(n):
              print("Prime Factors -->")
              for i in range(1,n):
                            if(n%i==0):
                                          print(i,end=", ")

n=int(input("Enter the Number :"))
print("Square Root:",sqrt(n))
print("Square:",sqr(n))
print("Cube:",cube(n))
print("Factorial:",fact(n))
prime(n)
prime_fact(n)

n=int(input("Enter a natural number: "))
if n>0:
    sum=0
    for i in range(0,n+1):
        fact=1
        for j in range(1,i+1):
            fact=fact*j
        sum=sum+(1/fact)
    print("Sum of the sequence is:",sum)
 

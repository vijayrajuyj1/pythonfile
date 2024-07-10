num=int(input("enter number"))
rev=0
n2=num
while num!=0:
   n1=num % 10
   rev=rev*10+n1
   num=num//10

if rev==n2:
    print("the number is pal")
else:
    print("not a pal")
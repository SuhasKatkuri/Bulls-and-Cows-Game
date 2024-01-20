import random
def check(a):
    if len(a)==3 and a[0]!=a[1] and a[1]!=a[2] and a[2]!=a[0]:
        return True
    else:
        print("Rewrite the Number as it is in wrong format")
        return False
def cows(c,d):
    x=0
    for i in range(3):
        if c[i]==d[i]:
            x+=1
    return x
def bulls(c,d):
    x=0
    if c[1]==d[2] or c[1]==d[0]:
        x+=1
    if c[2]==d[1] or c[2]==d[0]:
        x+=1
    if c[0]==d[1] or c[0]==d[2]:
        x+=1
    return x
c=[0]*3
c[0]=random.randint(1,9)
while True:
    c[1]=random.randint(1,9)
    if c[1]!=c[0]:
        break
while True:
    c[2]=random.randint(1,9)
    if c[2]!=c[0] and c[2]!=c[1]:
        break
b=str(c[0])+str(c[1])+str(c[2])
f=0
n=int(input("Enter Number of tries : "))
m=n
while(n):
    a=input("Choose a Number : ")
    if check(a):
        print("Number of cows : ",cows(a,b))
        print("Number of bulls : ",bulls(a,b))
        if cows(a,b)==3:
            print("You guessed correctly in ",m-n," tries")
            f=1
            break
        n-=1
if f!=1:
    print("You haven't guessed correctly in ",m," tries and number is",b)
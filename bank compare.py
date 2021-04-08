p=int(input())
t=int(input())
n1=int(input())
a=[]
b=[]
for i in range(n1):
    y,r=list(map(float,input().split()))
    x=(1+r)**(y*12)
    emi=(p*r)/(1-1/x)
    a.append(emi*y*12)
n2=int(input())
for i in range(n2):
    y1,r1=list(map(float,input().split()))
    x1=(1+r1)**(y1*12)
    em=(p*r1)/(1-1/x1)
    b.append(em*y1*12)
if (sum(a)<sum(b)):
    print("Bank A")
else:
    print("Bank B")

    
    

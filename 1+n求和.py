#1+(1+2)+(1+2+3)+...+(1+2+3+...n)
n=int(input("n="))
s=0
t=0
for i in range(1,n+1):
    t+=i
    s+=t
print(s)
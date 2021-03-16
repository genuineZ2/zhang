#ax^2+bx+c=0
import math
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
dlt=b*b-4*a*c
if dlt>=0:
    x1=(-b+math.sqrt(dlt))/2/a
    x2=(-b-math.sqrt(dlt))/2/a
    if dlt==0:
        print("有唯一根",x1)
    else:
        print("x1=",x1,"x2=",x2)
else:
    print("无实数根")
import math
a=int(input("輸入係數a:"))
b=int(input("輸入係數b:"))
c=int(input("輸入係數c:"))
r=math.sqrt((b**2)-4*a*c)
x1=(-b+r)/2*a
x2=(-b-r)/2*a
print("方程式的根為:X1=",x1,"X2=",x2)

a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
if a + b > c :
    import math
    p=(a+b+c)/2
    k=(p*(p-a)*(p-b)*(p-c))**2
    s=math.sqrt(k)
    print(s)
else:
    print("Khong phai la tam giac")
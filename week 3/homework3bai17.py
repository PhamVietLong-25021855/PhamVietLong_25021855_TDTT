a=int(input("Nhập vào cạnh thứ nhất:"))
b=int(input("Nhập vào cạnh thứ hai:"))
c=int(input("Nhập vào cạnh thứ ba:"))
if a+b>c and a+c>b and b+c>a and a==b==c:
    print("Tam giác đều")
elif a+b>c and a+c>b and b+c>a and a==b !=c or b==c !=a or c==a !=b:
    print("tam giác cân")
elif a+b>c and a+c>b and b+c>a and a != b != c:
    print("Tam giác thường")
else:
    print("Không phải tam giác")
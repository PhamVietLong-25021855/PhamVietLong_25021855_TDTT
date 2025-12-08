a=int(input("Nhập vào số thứ nhất:"))
b=int(input("Nhập vào số thứ hai:"))
c=int(input("Nhập vào số thứ ba:"))
d=int(input("Nhập vào số thứ tư:"))
largest=a
if b>largest:
    largest = b
if c>largest:
    largest = c
if d>largest:
    largest = d
print("Số nguyên lớn nhất là",largest)
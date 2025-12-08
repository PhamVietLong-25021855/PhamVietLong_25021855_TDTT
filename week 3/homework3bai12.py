n=int(input("Nhập vào một số nguyên dương n là năm:"))
if (n%4==0 and n%100 !=0) or n%400==0 :
    print("Năm đó là năm nhuận")
else:
    print("Năm đó không phải năm nhuận")

Năm=int(input("Năm: "))
if Năm%400==0 or Năm%4==0 and Năm%100!=0:
    print("Năm đó là năm nhuận")
else:
    print("Năm đó không phải năm nhuận")
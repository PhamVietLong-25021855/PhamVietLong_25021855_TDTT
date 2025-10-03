a=float(input("chieu rong:"))
b=float(input("chieu dai:"))
pi=3.14
r=float(input("ban kinh khu vui choi:"))
dien_tich_trong_cay=a*b-pi*r**2
if a/2>=r:
    print ("dien_tich_trong_cay=",f"{dien_tich_trong_cay:.2f}")
else:
    print("sai de bai")
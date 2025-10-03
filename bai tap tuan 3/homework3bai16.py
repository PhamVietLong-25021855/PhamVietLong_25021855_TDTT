n=float(input("Nhap vao mot so thuc:"))
nguyen=int(n)
thap_phan=n-nguyen 
# Lam tron xuong 
if n >= 0:
    floor_n=nguyen 
else:
    floor_n=nguyen if thap_phan==0 else nguyen - 1
# Lam tron len 
if n >=0 :
    celi_n=nguyen if thap_phan ==0 else nguyen + 1 
else:
    celi_n=nguyen 
# Lam tron gan nhat 
if thap_phan >= 0.5:
    round_n=nguyen +1 
elif thap_phan <=0.5 :
    round_n=nguyen - 1
else:
    round_x=nguyen
print(floor_n,celi_n,round_n)



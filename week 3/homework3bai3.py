def kiem_tra_luy_thua_cua_2_bitwise(n):
    n=int(input("n="))
    return n>0 and (n & (n-1)==0)
print(kiem_tra_luy_thua_cua_2_bitwise(n="n"))
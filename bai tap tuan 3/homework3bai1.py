def dao_nguoc_chu_so(n):
   chuoi_so = str(n)

  
   chuoi_dao_nguoc = chuoi_so[::-1]

  
   print(f"Số đảo ngược của {n} là: {chuoi_dao_nguoc}")


try:
  so_nhap = int(input("Nhập một số nguyên: "))
  dao_nguoc_chu_so(so_nhap)
except ValueError:
  print("Vui lòng nhập một số nguyên hợp lệ.")
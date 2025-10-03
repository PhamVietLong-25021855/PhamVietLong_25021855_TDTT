so_dien=int(input("Nhập vào số điện đã sử dụng(kWh):"))
if 0 <= so_dien <= 50 :
    print(so_dien*1500,"đồng")
elif 51 <= so_dien <= 100:
    print(50*1500+(so_dien-50)*2000,"đồng")
else:
    print(50*1500+50*2000+(so_dien-100)*3000,"đồng")
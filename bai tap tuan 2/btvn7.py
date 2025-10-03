van_ban=input("nhap vao mot van ban: ")
danh_sach_tu=van_ban.split()
so_tu=len(danh_sach_tu)
if so_tu >= 20:
    print("chu cai thu 5 duoc in ra la:",danh_sach_tu[4])
    print("chu cai thu 9 duoc in ra la:",danh_sach_tu[8])
else:
    print("khong thoa man yeu cau de bai")
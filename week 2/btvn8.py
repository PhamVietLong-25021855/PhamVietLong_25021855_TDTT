Ten_chu_ho=input("Ho va ten chu ho: ")
chi_so_dien_ke_thang_truoc=int(input("chi so thang truoc:"))
chi_so_dien_ke_thang_nay=int(input("chi so dien thang nay:"))
so_dien_cua_chu_ho=chi_so_dien_ke_thang_nay-chi_so_dien_ke_thang_truoc
if 0 < so_dien_cua_chu_ho <= 50:
   print("Ho va ten",Ten_chu_ho)
   print("Tien phai tra",round((so_dien_cua_chu_ho*1984*1.08)))
elif 51 <= so_dien_cua_chu_ho <=100:
   print("Ho va ten",Ten_chu_ho)
   print("Tien phai tra",round((50*1984+(so_dien_cua_chu_ho-50)*2050)*1.08))
elif 101 <= so_dien_cua_chu_ho <= 200:
   print("Ho va ten",Ten_chu_ho)
   print("Tien phai tra",round((50*1984+50*2050+(so_dien_cua_chu_ho-100)*2380)*1.08))
elif 201 <= so_dien_cua_chu_ho <= 300:
   print("Ho va ten",Ten_chu_ho)
   print("Tien phai tra",round((50*1984+50*2050+100*2380+(so_dien_cua_chu_ho-200)*2998)*1.08))
elif 301 <= so_dien_cua_chu_ho <= 400:
   print("Ho va ten",Ten_chu_ho)
   print("Tien phai tra",round((50*1984+50*2050+100*2380+100*2998+(so_dien_cua_chu_ho-300)*3350)*1.08))
elif 401 <= so_dien_cua_chu_ho :
   print("Ho va ten",Ten_chu_ho)
   print("Tien phai tra",round((50*1984+50*2050+100*2380+100*2998+100*3350+(so_dien_cua_chu_ho-400))*1.08))
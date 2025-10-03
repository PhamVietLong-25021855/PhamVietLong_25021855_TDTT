diem_hoc_luc=float(input("Điểm học lực:"))
if diem_hoc_luc >= 8:
    print("Học lực giỏi")
elif 6.5 <= diem_hoc_luc < 8 :
    print("Học lực khá")
elif 5 <= diem_hoc_luc < 6.5 :
    print("Học lực trung bình")
else:
    print("Học lực yếu")
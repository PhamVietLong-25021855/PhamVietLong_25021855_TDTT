x=float(input("Giá của chiếc đồng hồ là(USD): "))
total_cost=x + 10 +x* 0.30 +x* 0.10
total_cost=round(total_cost, 2)

print(f"Tổng số tiền Đạt phải trả ${total_cost:.2f}")

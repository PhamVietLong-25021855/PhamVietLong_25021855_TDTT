a =5
b =10
print(f"Trước khi hoán đổi:a={a},b={b}")
a = a ^ b
b = a ^ b
a = a ^ b 
print(f"Sau khi hoán đổi : a = {a}, b = {b}")
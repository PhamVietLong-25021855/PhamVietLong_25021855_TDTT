# phương trình y = ax + b
a=int(input("a="))
b=int(input("b="))
if a==0 and b==0 :
    print("Phương trình có vô số nghiệm")
elif a==0 and b != 0:
    print("Phương trình vô nghiệm")
else:
    print(f"Phương trình có nghiệm x= {-b/a:.2f}")
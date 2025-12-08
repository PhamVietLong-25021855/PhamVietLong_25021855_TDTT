names_input=input('Nhập tên 3 người(cách nhau bằng dấu cách):')
names=names_input.split()
if len(names) !=3:
    print("Vui lòng nhập đúng 3 tên !")
else :
    print(f"Hi {names[2]},{names[1]},{names[0]}.")
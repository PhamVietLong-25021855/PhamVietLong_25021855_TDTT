char=input("Nhap vao mot ki tu chu cai thuong(a-z): ")
if len(char) ==1 and 'a' <= char <= 'z':
    unicode_code=ord(char)
    print(f"Mã Unicode của '{char}' là : {unicode_code} ")


    upper_char_code=unicode_code - 32 # khoảng cách giữa chữ thương và hoa là 32
    upper_char = chr(upper_char_code)



    print(f"Kí tự hoa tương ứng là: '{upper_char}'")
    print(f"Mã Unicode của '{upper_char}' là: {ord(upper_char)}")
else:
    print("Vui lòng nhập đúng một kí tự chữ cái thường từ a đén z!")

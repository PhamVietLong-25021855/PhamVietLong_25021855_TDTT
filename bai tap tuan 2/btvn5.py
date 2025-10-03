c=input("Nhap vao mot chu cai hoa: ")
if c=='A':
    print("chu cai lien truoc 'a' la : z")
elif 'B'<= c <='Z':
    ch=chr(ord(c.lower())-1)
    print(f"chu cai lien truoc {c.lower()} la: {ch}")
else:
    print("ban chua nhap dung chu cai hoa.")
ki_tu=input("nhap vao mot chu cai tu a den z:")
chu_hoa=ki_tu.upper()
chu_thuong=ki_tu.lower()
if ki_tu==chu_hoa and ki_tu.isalpha():
    print("chu_thuong",chu_thuong)
elif ki_tu==chu_thuong and ki_tu.isalpha():
    print("chu_hoa",chu_hoa)

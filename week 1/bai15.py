def star_number(n):
    """
    Tính số sao thứ n (star number).
    Số sao là số hình học trung tâm đại diện cho hình lục giác có tâm 
    
    Công thức: S(n) = 6 * n * (n - 1) + 1

    Args:
        n (int): số nguyên dương

    Returns:
        int: số sao thứ n
    """
    if n <= 0:
        raise ValueError("n phải là số nguyên dương")

    return 6 * n * (n - 1) + 1


def main():
    """Hàm chính: nhập dữ liệu từ người dùng và in kết quả."""
    try:
        n = int(input("Nhập số nguyên dương n: "))

        if n <= 0:
            print("Vui lòng nhập số nguyên dương!")
            return

        print(f"Số sao thứ {n} là: {star_number(n)}")

    except ValueError:
        print("Giá trị nhập không hợp lệ, vui lòng nhập một số nguyên dương.")


if __name__ == "__main__":
    main()
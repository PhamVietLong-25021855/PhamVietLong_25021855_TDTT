def rubik_stickers(n):
    """
    Tính số lượng miếng dán cần thiết cho khối Rubik cạnh n.

    Args:
        n (int): Độ dài cạnh của khối Rubik

    Returns:
        int: Số lượng miếng dán cần thiết
    """
    return 6 * (n ** 2)


# Kiểm tra với các ví dụ
for i in range(1, 5):
    print(f"Khối Rubik {i}x{i}x{i}: {rubik_stickers(i)} miếng dán")
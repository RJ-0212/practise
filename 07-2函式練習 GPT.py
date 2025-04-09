def calculate_area(shape, values):
    """計算圓形或矩形的面積"""
    if shape == "circle":
        radius = values  # 半徑
        return 3.14159 * (radius ** 2)

    elif shape == "rectangle":
        length, width = values  # 長、寬
        return length * width

    else:
        return "不支援的形狀類型"


# 測試函式
print(calculate_area("circle", 5))  # 輸出：78.53975（圓形，半徑 5）
print(calculate_area("rectangle", (4, 6)))  # 輸出：24（矩形，長 4、寬 6）
print(calculate_area("triangle", (3, 5)))  # 輸出：不支援的形狀類型

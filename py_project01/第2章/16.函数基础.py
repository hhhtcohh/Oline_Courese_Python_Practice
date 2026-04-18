def circle_area(r) :
    """
    计算圆的面积
    :param r: 半径
    :return: 面积
    """
    pi = 3.14159
    area = pi * r * r
    return area
print(circle_area(5))
print(circle_area(10))

def circle_area_len(r) :
    """
    计算圆的面积和周长
    :param r: 半径
    :return: 面积和周长
    """
    pi = 3.14159
    return round(pi * r * r, 2),round(2 * pi * r, 2)
print(circle_area_len(5))
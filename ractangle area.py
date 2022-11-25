def rectangle_area(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int):
    l1 = ax2 - ax1
    l2 = bx2 - bx1
    b1 = ay2 - ay1
    b2 = by2 - by1
    a1 = l1 * b1
    a2 = l2 * b2
    total_area = a1 + a2 - max(min(ax2, bx2) - max(ax1, bx1), 0) * max(min(ay2, by2)- max(ay1, by1), 0)
    print(total_area)


rectangle_area(-3, 0, 3, 4, 0, -1, 9, 2)

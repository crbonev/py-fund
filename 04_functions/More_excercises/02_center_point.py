x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def center_point(xx, yy, xxx, yyy):
    point_one = (int(xx), int(yy))
    point_two = (int(xxx), int(yyy))
    result1 = abs(xx) + abs(yy)
    result2 = abs(xxx) + abs(yyy)
    if result1 <= result2:
        return point_one
    else:
        return point_two


print(center_point(x1, y1, x2, y2))

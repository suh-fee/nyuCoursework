# class Accumulator(object):
#     def __init__(self, starting_point = 0):
#         self.int = starting_point
#
#     def increment(self):
#         self.int += 1
#
#
# my_value = Accumulator()
# print(my_value.int)
# my_value.increment()
# print(my_value.int)


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        representation = "x cord " + str(self.x) + " " + "y cord: " + str(self.y)
        return representation

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def distance(self, point):
        value = ((self.x - point.x) ** 2) + ((self.y - point.y) ** 2)
        value = value ** (1/2)
        return value


def main():
    point1 = Point(0, 1)
    point2 = Point(0, 3)
    point1.distance(point2)
    print(point1)
    print(point2)
    point3 = point1 + point2
    print(point3)

main()
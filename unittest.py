import unittest
import math


class TriangleNotValidArgumentException(Exception):
    pass


class TriangleNotExistException(Exception):
    pass


class Triangle:

    def __init__(self, coordinates):
        if self._valid_arguments(coordinates):
            if self._valid_triangle(coordinates):
                self.a, self.b, self.c = [x for x in coordinates]

    def _valid_triangle(self, coordinates):
        if 2 * max(coordinates) >= sum(coordinates) or sum([x for x in coordinates if x > 0]) != sum(coordinates):
            raise TriangleNotExistException("Can`t create triangle with this arguments")
        else:
            print(coordinates)
            return True

    def _valid_arguments(self, coordinates):
        try:
            if type(coordinates) != tuple or len(coordinates) != 3 or sum([x for x in coordinates if isinstance(x, (int,float))]) != sum(coordinates):
                raise TriangleNotValidArgumentException("Not valid arguments")
            else:
                return True
        except:
            raise TriangleNotValidArgumentException("Not valid arguments")

    def get_area(self):
        perimetr = (self.a+self.b+self.c)/2
        S = math.sqrt(perimetr * (perimetr - self.a) * (perimetr - self.b) * (perimetr - self.c))
        return S


class TriangleTest(unittest.TestCase):

    def test_triangle(self):
        self.assertEquals(Triangle((3, 4, 5)).get_area(), 6.0)

    def test_not_valid_arguments(self):
        with self.assertRaises(TriangleNotValidArgumentException):
            Triangle((2,3))

    def test_not_valid_triangle(self):
        with self.assertRaises(TriangleNotExistException):
            Triangle((1,2,3))






valid_test_data = [
    (3, 4, 5),
    (26, 25, 3),
    (30, 29, 5),
    (87, 55, 34),
    (120, 109, 13),
    (123, 122, 5)
]
for data in valid_test_data:
    print(Triangle(data).get_area())

not_valid_triangle = [
    (1, 2, 3),
    (1, 1, 2),
    (7, 7, 15),
    (100, 7, 90),
    (17, 18, 35),
    (127, 17, 33),
    (145, 166, 700),
    (1000, 2000, 1),
    (717, 17, 7),
    (0, 7, 7),
    (-7, 7, 7)
]
for data in not_valid_triangle:
    try:
        Triangle(data)

    except TriangleNotExistException as e:
        print(e)
#
# not_valid_arguments = [
#     ('3', 4, 5),
#     ('a', 2, 3),
#     'string',
#     (7, 2),
#     (7, 7, 7, 7),
#     10
# ]
# for data in not_valid_arguments:
#     try:
#         Triangle(data)
#     except TriangleNotValidArgumentException as e:
#         print(e)

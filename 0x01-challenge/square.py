#!/usr/bin/python3
""" Module for Square class"""

class Square:
    """ Square class """

    def __init__(self, width=0, height=0):
        """ Instantiation of class """
        self.width = width
        self.height = height

    def area_of_my_square(self) -> int:
        """ Calculate the area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self) -> int:
        """ Calculate the perimeter of the square """
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        """ Printable representation """
        return f"{self.width}/{self.height}"

if __name__ == "__main__":
    """ Create a Square object and print its details """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())


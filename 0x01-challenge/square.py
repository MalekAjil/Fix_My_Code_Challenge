#!/usr/bin/python3
"""Square Model"""


class square():
    """Represents a Square"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """the intializer"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """The Pirameter of the Square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """The string representation"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())

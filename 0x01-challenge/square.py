#!/usr/bin/python3
"""Square Module"""


class square():
    """Square Class"""
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initializer"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """Peramiter of of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """String representation"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """start point"""
    s = square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())

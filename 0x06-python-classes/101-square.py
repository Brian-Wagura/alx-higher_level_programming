class Square:
    """
    A class that defines a square.

    Attributes:
        size(int): The size of the square
        position(tuple): The position of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size(int, optional): The size of the square. Default to 0
            position(tule, optional): The position of the square. Defaults to (0, 0)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        int: The size of the square
        """

        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size to set

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        tuple: The position of the square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Sets the position of the square

        Args:
            value(tuple): The position to set.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square
        """
        return (self.size ** 2)

    def my_print(self):
        """
        Prints the square with the charcter #

        If size is equal to 0, prints an empty line. Position is used
        by using space.
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)


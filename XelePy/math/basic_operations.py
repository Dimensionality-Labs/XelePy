import warnings

def add(x, y):
    """
    Adds two numbers together and returns the result.
    
    Parameters:
        x (int): The first number to be added.
        y (int): The second number to be added.
    
    Returns:
        int: The sum of x and y.
    """
    return x + y

def subtract(x, y):
    """
    Subtract two numbers.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The difference between x and y.
    """
    return x - y

def multiply(x, y):
    """
    Multiplies two numbers and returns the result.

    Parameters:
        x (float): The first number to be multiplied.
        y (float): The second number to be multiplied.

    Returns:
        float: The product of x and y.
    """
    return x * y

def divide(x, y):
    """
    Divide two numbers and return the result.

    Parameters:
        x (int or float): The numerator.
        y (int or float): The denominator.

    Returns:
        float: The quotient of x divided by y.
    """
    return x / y

def power(x, y):
    """
    Calculate the power of a number.

    Parameters:
        x (int or float): The base number.
        y (int or float): The exponent.

    Returns:
        int or float: The result of raising x to the power of y.
    """
    return x ** y

def square(x):
    """
    Calculates the square of a given number.

    Args:
        x (int or float): The number to be squared.

    Returns:
        int or float: The square of the given number.
    """
    return x ** 2

def sqrt(x, asInt=False):
    """
        Calculates the square root of a number.

        Parameters:
            x (float): The number to calculate the square root of.
            asInt (bool, optional): If True, the result will be rounded to the nearest integer. 
                                    If False, the result will be a floating-point number. 
                                    Defaults to False.

        Returns:
            float or int: The square root of the number. If asInt is True, the result will be an integer.
                        If asInt is False, the result will be a floating-point number.
    """
    if asInt == True:
        try:
            return int(x ** 0.5)
        except:
            warnings.warn("Cannot round to an integer. Returning float instead.")
            return x ** 0.5
    else:
        return x ** 0.5

def reciprocal(x):
    """
        Calculates the reciprocal of a number.

        Parameters:
            x (float): The number to calculate the reciprocal of.

        Returns:
            float: The reciprocal of the number.
    """
    return 1 / x

def mod(x, y):
    """
        Calculates the modulus of two numbers.

        Parameters:
            x (int or float): The first number.
            y (int or float): The second number.

        Returns:
            int or float: The modulus of the two numbers.
    """
    return x % y

def abs(x):
    """
        Calculates the absolute value of a number.

        Parameters:
            x (int or float): The number to calculate the absolute value of.

        Returns:
            int or float: The absolute value of the number.
    """
    return x if x >= 0 else -x

def floor(x):
    return int(x)

def ceil(x):
    return int(x + 1)

if __name__ == '__main__':
    print(add(2, 3))
    print(subtract(2, 3))
    print(multiply(2, 3))
    print(divide(2, 3))
    print(power(2, 3))
    print(square(2))
    print(sqrt(25))
    print(sqrt(21, asInt=True))
    print(reciprocal(2))
    print(mod(2, 3))
    print(abs(-2))


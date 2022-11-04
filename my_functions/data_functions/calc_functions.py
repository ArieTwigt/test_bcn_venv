


def calc_circle(diameter):

    """Calculate the area of a circle.

    Args:

        diameter (float): Diameter of the circle.

    Returns:

        float: Area of the circle.

    """

    return 3.14 * (diameter / 2) ** 2


def calc_pythagoras():

    """Calculate the hypotenuse of a right triangle.

    Returns:

        float: Hypotenuse of the right triangle.

    """

    a = float(input("Enter the length of side a: "))

    b = float(input("Enter the length of side b: "))

    return (a ** 2 + b ** 2) ** 0.5
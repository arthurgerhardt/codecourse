def sum_positive_and_negative(positive_number, negative_number):
    """Sums a positive and a negative number.

    Args:
        positive_number: A positive number.
        negative_number: A negative number.

    Returns:
        The sum of the two numbers.
        Raises TypeError if either input is not a number.
        Raises ValueError if inputs are not a positive and a negative number respectively.

    """

    if not isinstance(positive_number, (int, float)) or not isinstance(negative_number, (int, float)):
        raise TypeError("Inputs must be numbers.")

    if positive_number < 0 or negative_number >= 0:
        raise ValueError("Inputs must be a positive and a negative number respectively.")


    return positive_number + negative_number



# Example usage:
try:
    result = sum_positive_and_negative(5, -3)
    print(f"The sum is: {result}")  # Output: The sum is: 2

    result = sum_positive_and_negative(10, -10)  # Output: 0
    print(f"The sum is: {result}")

    result = sum_positive_and_negative(2.5, -1.5)  # Output: 1.0
    print(f"The sum is: {result}")


    result = sum_positive_and_negative(-5, 3)  # Raises ValueError
except ValueError as e:
    print(e) # Output: Inputs must be a positive and a negative number respectively.

except TypeError as e:
    print(e)


try:
    result = sum_positive_and_negative("5", -3)  # Raises TypeError
except ValueError as e:
    print(e)

except TypeError as e:
    print(e) # Output: Inputs must be numbers.


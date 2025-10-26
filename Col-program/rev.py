def reverse_number(num: int) -> int:
    """
    Reverse the digits of a given integer.

    This function reverses the order of digits in the input integer while
    preserving the sign. Leading zeros are handled naturally as they don't
    affect the numeric value.

    Args:
        num (int): The integer to reverse

    Returns:
        int: The reversed integer

    Raises:
        TypeError: If input is not an integer
        OverflowError: If the reversed number exceeds integer limits

    Examples:
        >>> reverse_number(123)
        321
        >>> reverse_number(-456)
        -654
        >>> reverse_number(0)
        0
        >>> reverse_number(120)
        21
    """
    if not isinstance(num, int):
        raise TypeError(f"Expected integer, got {type(num).__name__}")

    # Store the sign and work with absolute value
    sign = -1 if num < 0 else 1
    num = abs(num)

    # Handle zero case
    if num == 0:
        return 0

    # Reverse the digits using mathematical operations
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10

    # Apply the original sign
    result = sign * reversed_num

    # Check for integer overflow (Python 3 handles large integers, but we'll check for safety)
    if result > 2**31 - 1 or result < -2**31:
        raise OverflowError("Reversed number exceeds integer limits")

    return result


def main() -> None:
    """
    Main function to handle user input and output for number reversal.
    """
    try:
        user_input = input("Enter an integer to reverse: ").strip()

        if not user_input:
            print("No input provided. Please enter an integer.")
            return

        # Try to convert input to integer
        try:
            number = int(user_input)
        except ValueError:
            print(f"Error: '{user_input}' is not a valid integer.")
            return

        reversed_num = reverse_number(number)
        print(f"Original number: {number}")
        print(f"Reversed number: {reversed_num}")

    except TypeError as e:
        print(f"Error: {e}")
    except OverflowError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except EOFError:
        print("\nInput stream ended.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()

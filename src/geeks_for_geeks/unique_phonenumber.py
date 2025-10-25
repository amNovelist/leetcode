def has_unique_digits_bits(phone_number: str) -> bool:
    # Initialize checker to 0
    checker = 0

    for digit in phone_number:
        # Convert char to int
        num = int(digit)
        # Create mask by shifting 1 to position num
        mask = 1 << num

        # If digit already seen, return False
        if checker & mask:
            return False

        # Mark digit as seen
        checker |= mask

    return True

has_unique_digits_bits("945381249")
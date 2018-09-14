# https://app.codesignal.com/arcade/intro/level-10/HJ2thsvjL25iCvvdm
def isMAC48Address(input_string):
    # Split into groups by dashes.
    groups = input_string.split("-")
    # Validate that we have exactly 6 groups.
    if len(groups) != 6:
        return False

    # Check if a group is a two digit hex value.
    def is_hex(group):
        hex_vals = "0123456789ABCDEF"
        # Two digits limit.
        if len(group) != 2:
            return False
        # The two values are in expected range.
        if group[0] in hex_vals and group[1] in hex_vals:
            return True
        # Anything else is not hex pair.
        return False

    # All groups must fulfill the is_hex condition.
    return all([is_hex(group) for group in groups])

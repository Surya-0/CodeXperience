def find_complement(num):
    # Calculate the bit length of the number
    bit_length = num.bit_length()
    print(bit_length)
    # Create a bitmask with all bits set to 1 of the same length as num
    bitmask = (1 << bit_length) - 1
    print(bitmask)

    # XOR num with the bitmask to get the complement
    complement = num ^ bitmask

    return complement


# Example usage
num = 5
print(find_complement(num))  # Output: 2
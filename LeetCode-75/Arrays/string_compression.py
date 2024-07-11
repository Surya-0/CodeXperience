from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        write = 0  # To write on the list, this should be finally returned
        i = 0  # iterator through the list

        while i < n:
            char = chars[i]
            count = 0

            # This is used to count the number of occurrences
            while i < n and chars[i] == char:
                i += 1
                count += 1

            # Time to write the characters
            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        # print(chars)
        return write




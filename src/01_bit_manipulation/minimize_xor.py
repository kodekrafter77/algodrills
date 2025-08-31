#!/usr/bin/env python3

from typing import List

# https://leetcode.com/problems/minimize-xor


class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Count set bits in num2 using built-in bin().count()
        target_bits = num2.bit_count()
        result = 0
        remaining_bits = target_bits

        # Phase 1: Match 1's from num1 starting from most significant bits
        # We iterate from bit 31 down to 0 (total 32 bits for integers)
        for i in range(31, -1, -1):
            # Check if num1 has a 1 at position i using bit mask
            current_bit = (num1 >> i) & 1
            if current_bit == 1 and remaining_bits > 0:
                # Set this bit in our result using OR operation
                result |= (1 << i)
                remaining_bits -= 1

        # Phase 2: If we need more 1's, add them in least significant positions
        # where num1 has 0's
        if remaining_bits > 0:
            for i in range(32):
                # Check if num1 has a 0 at position i
                current_bit = (num1 >> i) & 1
                if current_bit == 0 and remaining_bits > 0:
                    result |= (1 << i)
                    remaining_bits -= 1

        return result


def main():
    s = Solution()
    print(s.minimizeXor(3, 5))
    print(s.minimizeXor(1, 12))


if __name__ == '__main__':
    main()

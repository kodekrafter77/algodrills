#!/usr/bin/env python3

from typing import List

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        # Outer loop: Iterate through each of the 32 bit positions
        for i in range(32):
            sum_of_bits_at_i = 0

            # Inner loop: For the current bit 'i', iterate through all numbers in the list
            for num in nums:
                # Check if the i-th bit is set for the current number
                if (num >> i) & 1:
                    sum_of_bits_at_i += 1

            # If the sum of bits at this position is not a multiple of 3,
            # it means the unique number has a '1' at this bit position.
            if sum_of_bits_at_i % 3 != 0:
                # Set the i-th bit in our result
                res |= (1 << i)

        # LeetCode needs to handle negative numbers correctly.
        # If the 31st bit is set, it's a negative number in two's complement.
        if (res >> 31) & 1:
            res -= (1 << 32)

        return res


def main():
    s = Solution()
    print(s.singleNumber([2,2,3,2]))
    print(s.singleNumber([0,1,0,1,0,1,99]))
    print(s.singleNumber([30000,500,100,30000,100,30000,100]))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

from typing import List

# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shifts = 0
        # The core idea is to find the common binary prefix of 'left' and 'right'.
        # Any bits that differ between them will eventually become zero when ANDed
        # over the range because at some point a number will flip that bit to 0.
        # We find this common prefix by right-shifting both numbers until they are equal.
        while left != right:
            left >>= 1
            right >>= 1
            shifts += 1
        # At this point, 'left' (and 'right') holds the common binary prefix.
        # To get the final answer, we must restore the prefix to its original magnitude
        # by left-shifting it by the number of shifts we performed.
        return left << shifts

    def rangeBitwiseAndLessOptimal(self, left: int, right: int) -> int:
        # As long as right is greater than left,
        # there is a difference in their binary representation.
        # We turn off the rightmost '1' bit of 'right'
        # until right is less than or equal to left.
        # This process effectively finds the common prefix.
        while right > left:
            right = right & (right - 1)
        return right


def main():
    s = Solution()
    print(s.rangeBitwiseAnd(5, 7))
    print(s.rangeBitwiseAnd(0, 0))
    print(s.rangeBitwiseAnd(1, 2147483647))


if __name__ == '__main__':
    main()

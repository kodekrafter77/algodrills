#!/usr/bin/env python3

from typing import List

# https://leetcode.com/problems/counting-bits/description/

class Solution:
    def countBits(self, n: int) -> List[int]:
        nbits = [0] * (n + 1)
        """
        The operation i >> 1 is the same as taking the number i and chopping off its rightmost bit.

        6 is 110. 6 >> 1 is 3, which is 11.
        
        7 is 111. 7 >> 1 is 3, which is 11.
        
        8 is 1000. 8 >> 1 is 4, which is 100.
        
        This means the number of 1s in i is just (the number of 1s in i >> 1) + (the value of the bit you just chopped off).
        
        The bit you just chopped off is simply 1 if i is odd, and 0 if i is even. You can get this value with the modulo operator: i % 2.
        """

        for i in range(1, n + 1):
            nbits[i] = nbits[i >> 1] + i % 2

        return nbits



def main():
    s = Solution()
    print(s.countBits(2))
    print(s.countBits(5))


if __name__ == '__main__':
    main()

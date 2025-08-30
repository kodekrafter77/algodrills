#!/usr/bin/env python3

from typing import List

# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            res ^= num

        return res


def main():
    s = Solution()
    print(s.singleNumber([4,1,2,1,2]))


if __name__ == '__main__':
    main()

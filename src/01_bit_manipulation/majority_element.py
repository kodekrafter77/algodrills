#!/usr/bin/env python3

from typing import List

# https://leetcode.com/problems/majority-element/


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        half_n = len(nums) // 2
        for i in range(32):
            count_bits_set = 0
            for num in nums:
                if (num >> i) & 1:
                    count_bits_set += 1
            if count_bits_set > half_n:
                res |= (1 << i)
        # Handle negative numbers using two's complement representation
        if (res >> 31) & 1:
            res -= (1 << 32)

        return res

    def majorityElementBoyerMooreVoting(self, nums: List[int]) -> int:
        count = 0
        candidate = None  # Start with no candidate

        for num in nums:
            if count == 0:
                # We have a new candidate
                candidate = num

            # The count update happens on every iteration
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


def main():
    s = Solution()
    print(s.majorityElement([3, 2, 3]))
    print(s.majorityElement([2,2,1,1,1,2,2]))


if __name__ == '__main__':
    main()

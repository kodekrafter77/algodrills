#!/usr/bin/env python3

# https://leetcode.com/problems/hamming-distance/


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # z = x ^ y
        # count = 0
        #
        # while z:
        #     z = z & (z - 1)
        #     count += 1
        #
        # return count
        return (x ^ y).bit_count()


def main():
    s = Solution()
    print(s.hammingDistance(1, 4))
    print(s.hammingDistance(3, 1))


if __name__ == '__main__':
    main()

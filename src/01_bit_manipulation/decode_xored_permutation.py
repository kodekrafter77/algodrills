#!/usr/bin/env python3

from typing import List

# https://leetcode.com/problems/decode-xored-permutation/description/


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1

        # Helper function for O(1) XOR sum calculation
        def xor_sum_up_to(num):
            mod = num % 4
            if mod == 0:
                return num
            elif mod == 1:
                return 1
            elif mod == 2:
                return num + 1
            else:  # mod == 3
                return 0

        # Step 1: Find perm[0] using the O(1) optimization
        total_xor_perm = xor_sum_up_to(n)

        xor_all_but_first_perm = 0
        for i in range(1, n - 1, 2):
            xor_all_but_first_perm ^= encoded[i]

        first_element = total_xor_perm ^ xor_all_but_first_perm

        # Step 2: The rest of the logic remains the same
        perm = [first_element]
        for i in range(n - 1):
            next_element = perm[i] ^ encoded[i]
            perm.append(next_element)

        return perm


def main():
    s = Solution()
    print(s.decode([3, 1]))
    print(s.decode([6, 5, 4, 6]))


if __name__ == '__main__':
    main()

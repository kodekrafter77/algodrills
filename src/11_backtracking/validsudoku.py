#!/usr/bin/env python3

from typing import List
from collections import defaultdict

# https://leetcode.com/problems/valid-sudoku


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Determines if a 9x9 Sudoku board is valid by checking rows, columns,
        and 3x3 sub-boxes in a single pass.
        """

        # --- Step 1: Initialize Data Structures ---
        # We use sets to efficiently check for duplicates.
        # `rows` and `cols` will be a list of 9 sets, one for each row/column.
        # `boxes` will be a dictionary where the key is a (box_row, box_col) tuple.
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = defaultdict(set)

        # --- Step 2: Single Pass Through the Board ---
        # Iterate through every cell (r, c) of the 9x9 board.
        for r in range(9):
            for c in range(9):
                num = board[r][c]

                # If the cell is empty, skip it.
                if num == '.':
                    continue

                # --- Step 3: Check for Duplicates ---

                # a) Check the current row
                if num in rows[r]:
                    return False  # Found a duplicate in the same row

                # b) Check the current column
                if num in cols[c]:
                    return False  # Found a duplicate in the same column

                # c) Check the current 3x3 box
                # Calculate the box ID using integer division.
                box_id = (r // 3, c // 3)
                if num in boxes[box_id]:
                    return False  # Found a duplicate in the same 3x3 box

                # --- Step 4: Add the Number to Sets ---
                # If no duplicates were found, add the current number to all
                # three sets to track it for future checks.
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_id].add(num)

        # --- Step 5: Return Result ---
        # If the loops complete without finding any duplicates, the board is valid.
        return True


def main():
    s = Solution()

    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(s.isValidSudoku(board))

    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(s.isValidSudoku(board))


if __name__ == '__main__':
    main()

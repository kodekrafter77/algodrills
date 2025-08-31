#!/usr/bin/env python3

from typing import List

# https://leetcode.com/problems/sudoku-solver


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solves the Sudoku puzzle by modifying the board in-place using a
        highly optimized backtracking algorithm.
        """
        # --- Step 1: Pre-computation / State Tracking ---
        # Create sets to track which numbers are in each row, column, and 3x3 box.
        # This allows for O(1) validity checks.
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Populate the sets with the initial numbers on the board.
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    box_id = (r // 3) * 3 + (c // 3)
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_id].add(num)

        # Start the backtracking process from the top-left cell (0, 0).
        self.backtrack(board, 0, 0, rows, cols, boxes)

    def backtrack(self, board: List[List[str]], r: int, c: int, rows: List[set], cols: List[set],
                  boxes: List[set]) -> bool:
        """
        The core recursive backtracking function, optimized to process cell by cell.
        """
        # --- Base Case (Success) ---
        # If we've gone past the last row, it means the entire board is filled.
        if r == 9:
            return True  # Solution found!

        # --- Calculate Next Position ---
        # Determine the coordinates of the next cell to process.
        next_r = r + (c + 1) // 9
        next_c = (c + 1) % 9

        # --- Recursive Step ---

        # If the current cell is already filled, move on to the next one.
        if board[r][c] != '.':
            return self.backtrack(board, next_r, next_c, rows, cols, boxes)

        # If the cell is empty, try placing each number from '1' to '9'.
        box_id = (r // 3) * 3 + (c // 3)
        for num_to_try in "123456789":

            # a) Check if the number is a valid placement in O(1) time.
            if (num_to_try not in rows[r] and
                    num_to_try not in cols[c] and
                    num_to_try not in boxes[box_id]):

                # b) Place the number and update our tracking sets.
                board[r][c] = num_to_try
                rows[r].add(num_to_try)
                cols[c].add(num_to_try)
                boxes[box_id].add(num_to_try)

                # c) Explore: Recurse to the next cell.
                if self.backtrack(board, next_r, next_c, rows, cols, boxes):
                    return True  # Solution found!

                # d) Undo the guess (Backtrack): If the recursion failed,
                # remove the number from the board and the tracking sets.
                board[r][c] = '.'
                rows[r].remove(num_to_try)
                cols[c].remove(num_to_try)
                boxes[box_id].remove(num_to_try)

        # If no number from '1' to '9' worked for this cell, this path is a failure.
        return False

def main():
    s = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s.solveSudoku(board)
    print(board)


if __name__ == '__main__':
    main()

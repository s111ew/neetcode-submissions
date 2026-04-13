class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizontals = []
        verticals = []
        boxes = []

        for i in range(9):
            horizontals.append(set())
            verticals.append(set())
            boxes.append(set())

        for y, line in enumerate(board):
            for x, num in enumerate(line):
                if num == ".":
                    continue
                box_idx = (y // 3) * 3 + (x // 3)
                if num in horizontals[y] or num in verticals[x] or num in boxes[box_idx]:
                    return False
                horizontals[y].add(num)
                verticals[x].add(num)
                boxes[box_idx].add(num)

        return True 

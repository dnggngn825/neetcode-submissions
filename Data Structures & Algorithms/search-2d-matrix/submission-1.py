class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nRow, nCol = len(matrix), len(matrix[0])
        if (target < matrix[0][0] or target > matrix[nRow-1][nCol-1]):
            return False
        rowIndex = int(nRow/2)
        top, down = nRow, 0
        while rowIndex != top and rowIndex != down:
            if (target == matrix[rowIndex][0]):
                return True
            elif (target < matrix[rowIndex][0]):
                top = rowIndex
                rowIndex = int((rowIndex+down)/2)
            else:
                down = rowIndex
                rowIndex = int((rowIndex+top)/2)

        colIndex = int(nCol/2)
        left, right = 0, nCol
        while colIndex != left and colIndex != right:
            if (target == matrix[rowIndex][colIndex]):
                return True
            elif (target < matrix[rowIndex][colIndex]):
                right = colIndex
                colIndex = int((left+ colIndex)/2)
            else:
                left = colIndex
                colIndex = int((right+colIndex)/2)
            
        return target == matrix[rowIndex][colIndex]
        
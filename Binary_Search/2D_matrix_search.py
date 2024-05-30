class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        m = len(matrix)
        n = len(matrix[0])
        high = m * n - 1
        while low <= high:
            mid = low + (high - low)//2
            row_num = mid//n
            col_num = mid%n
            if matrix[row_num][col_num] == target:
                return True
            elif matrix[row_num][col_num] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
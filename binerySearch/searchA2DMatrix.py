class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols=len(matrix),len(matrix[0])

        left,right=0,rows-1

        row=0

        while left<=right:
            mid=(left)+(right-left)//2

            if matrix[mid][0]<=target:
                row=mid
                left=mid+1
            
            else:
                right=mid-1
        
        left,right=0,cols-1

        while left<=right:
            mid=left+(right-left)//2

            if matrix[row][mid]==target:
                return True
            
            elif matrix[row][mid]<target:
                left=mid+1
            
            else:
                right=mid-1
        
        return False

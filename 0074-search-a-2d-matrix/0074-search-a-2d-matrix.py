class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        n,m=len(mat),len(mat[0])
        fr,lr=0,n-1
        row=-1
        while fr<=lr:
            mid=fr+(lr-fr)//2
            if mat[mid][0]<=target:
                row=mid
                fr=mid+1
            else:
                lr=mid-1
        if row==-1:
            return False
        l,r=0,m-1
        while l<=r:
            mid=l+(r-l)//2
            if mat[row][mid]==target:
                return True
            elif mat[row][mid]<target:
                l=mid+1
            else:
                r=mid-1
        return False
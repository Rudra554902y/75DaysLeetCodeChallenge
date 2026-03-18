class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        ans=float('-inf')
        n=len(heights)
        for i in range(n+1):
            curr=heights[i] if i<n else float('-inf')
            while stack and heights[stack[-1]]>curr:
                mid=stack.pop()
                width=i-mid
                height=heights[mid]
                ans=max(ans,width*height)
            stack.append(i)
        return ans
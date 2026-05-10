class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        n = len(heights)

        for i in range(n):

            while stack and heights[stack[-1]] > heights[i]:

                height = heights[stack.pop()]

                width = i if not stack else i - stack[-1] - 1

                ans = max(ans, height * width)

            stack.append(i)

        while stack:

            height = heights[stack.pop()]

            width = n if not stack else n - stack[-1] - 1

            ans = max(ans, height * width)

        return ans
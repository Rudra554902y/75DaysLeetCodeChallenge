class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hp={}
        stack=[]
        res=[]
        for i in nums2[::-1]:
            while stack and stack[-1]<=i:
                stack.pop()
            if stack:
                hp[i]=stack[-1]
            else:
                hp[i]=-1
            stack.append(i)
        for i in nums1:
            res+=[hp[i]]
        return res
        print(hp)
        
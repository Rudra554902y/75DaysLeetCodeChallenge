class Solution:
    def sortColors(self, nums: List[int]) -> None:
        co = {}
        for i in range(len(nums)):
            co[nums[i]] = co.get(nums[i], 0) + 1
        
        idx = 0

        for color in range(3):
            fr = co.get(color, 0)
            nums[idx : idx + fr] = [color] * fr
            idx += fr
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] == target:
#                 return mid
#             if nums[left] <= nums[mid]:
#                 # Left half is sorted
#                 if nums[left] <= target < nums[mid]:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             else:
#                 # Right half is sorted
#                 if nums[mid] < target <= nums[right]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#         return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target: return mid
            elif nums[l]<=nums[mid]:
                l,r=(l,mid-1) if nums[l]<=target<=nums[mid] else (mid+1,r)
            else: 
                l,r=(mid+1, r) if nums[mid]<=target<=nums[r] else (l,mid-1)
        return -1
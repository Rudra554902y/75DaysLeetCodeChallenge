import bisect
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(l,mid,r,arr):
            count=0
            res=[]
            i=l
            j=mid+1
            for i in range(l,mid+1):
                while j<=r and arr[i]>2*arr[j]:
                    j+=1
                count+=j-(mid+1)
            i=l
            j=mid+1

            while i<=mid and j<=r:
                if arr[i]<=arr[j]:
                    res.append(arr[i])
                    i+=1
                else:
                    res.append(arr[j])
                    j+=1
            while i<=mid:
                res.append(arr[i])
                i+=1
            while j<=r:
                res.append(arr[j])
                j+=1
            for k in range(r-l+1):
                arr[l+k]=res[k]
            return count
                
                        
        def merge_sort(i,j,arr):
            count=0
            if i<j:
                mid=(i+j)//2
                count+=merge_sort(i,mid,arr)
                count+=merge_sort(mid+1,j,arr)
                count+=merge(i,mid,j,arr)
            return count
        return merge_sort(0,len(nums)-1,nums)
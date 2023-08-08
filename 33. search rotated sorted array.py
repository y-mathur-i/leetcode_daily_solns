class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def getAns(nums,low,high):
            if low > high:
                return -1
            mid = (high+low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[low]:
                if nums[low] <= target <= nums[mid]:
                    return getAns(nums,low,mid-1)
                return getAns(nums,mid+1,high)
            if nums[mid] <= target <= nums[high]:
                return getAns(nums,mid+1,high)
            return getAns(nums,low,mid-1)
        res = getAns(nums,0,len(nums)-1)
        return res 
            
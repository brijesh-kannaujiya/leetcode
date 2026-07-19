class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(0,len(nums)-2,1):
            if i>0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            oldsum = nums[i]*-1
            while left < right :
                newsum = nums[left]+nums[right]
                if oldsum == newsum :
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                        continue 
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
                        continue
                elif oldsum < newsum:
                    right-=1
                else:
                    left+=1
        return res        




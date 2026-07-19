class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        j=0
        count = 1
        res = 1
        while i<len(nums): 
            if nums[i] == nums[i-1]:
                res+=1
            else:
                res = 1
            if res<=2:
                j+=1
                nums[j] = nums[i]
                count +=1
            i+=1
        return count

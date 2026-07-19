class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cm =1
        offcer = 0
        n = len(nums)
        while cm < n :
            if(nums[cm] == nums[cm-1]):
                cm+=1
                continue
            offcer+=1
            nums[offcer] = nums[cm]
            cm+=1
        return offcer + 1
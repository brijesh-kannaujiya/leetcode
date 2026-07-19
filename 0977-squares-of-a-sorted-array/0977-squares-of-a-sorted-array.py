class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = 0
        number = len(nums)
        right = number -1
        result = [0]*number
        index = number -1
        while left <= right :
            leftsq = nums[left] * nums[left]
            rightsq = nums[right] * nums[right]

            if(leftsq > rightsq):
               result[index] =  leftsq
               left += 1
            else :
                result[index] =  rightsq
                right -= 1
            index -= 1
        return result
        
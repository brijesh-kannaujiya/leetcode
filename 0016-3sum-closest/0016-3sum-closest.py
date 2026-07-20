class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        max_diff = float('inf')
        closest_sum = 0
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1
            while left < right:
                cur_sum = nums[i]+nums[left]+nums[right]
                absdiff = abs(cur_sum-target)
                if max_diff > absdiff :
                    max_diff = absdiff
                    closest_sum = cur_sum
                if cur_sum == target:
                    left+=1
                    right-=1
                elif cur_sum < target:
                    left+=1
                else:
                    right-=1
        return closest_sum
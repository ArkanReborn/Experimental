class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        minnum = 0
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = 1
            else:
                seen[nums[i]] += 1
            minval = i
        print(seen.items())
        print(minval)
        for key, value in seen.items():
            if value < minval:
                minnum = key
                minval = value
        return minnum
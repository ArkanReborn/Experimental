class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = {}
        ans = []
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = 1
            else:
                seen[nums[i]] += 1
        print(seen.items())
        for keys, values in seen.items():
            if values == 1:
                ans.append(keys)
        return ans
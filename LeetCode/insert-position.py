class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > nums[-1]:
            return len(nums)
        for i in range(len(nums)): # 0-3
            if nums[i] == target:
                #print("This ran!")
                return i
            if i + 1 < len(nums) and ((nums[i] < target) and (target < nums[i + 1])):
                #print("This runs!")
                return i + 1
            #print(nums[i])   
        return 0 # Default return if neither if statement filled the condition
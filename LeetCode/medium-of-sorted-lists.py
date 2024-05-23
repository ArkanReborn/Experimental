class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        mergedList = sorted(nums1 + nums2)
        mergedLen = len(mergedList)
        midNum = mergedLen // 2
        return (mergedList[midNum] + mergedList[midNum - 1]) / 2.0 if mergedLen % 2 == 0 else mergedList[midNum]

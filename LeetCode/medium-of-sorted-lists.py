class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        mergedList = nums1 + nums2
        mergedList.sort()
        total = 0
        if len(mergedList) > 1:
            for i in mergedList:
                print(i)
                if (mergedList[i - 1] <= 0):
                    del mergedList[i]

            lstLen = len(mergedList)

            for i in mergedList:
                total += mergedList[i - 1]
            print(total)
            print(mergedList)
            print(lstLen)
        else:
            return mergedList[0]
        return total / float(lstLen)
# Not finished yet. It is a work in progress
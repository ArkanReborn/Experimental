from collections import Counter

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        freq_map = Counter(arr)
        freq_list = sorted(freq_map.items(), key=lambda x: x[1])

        unique_count = len(freq_list)
        for num, count in freq_list:
            if k >= count:
                k -= count
                unique_count -= 1
            else:
                break
        return unique_count
    # Runtime 405ms. Beats 48.76% of Python users
    # Memory 36.67 MB. Beats 32.23% of Python users
        
    
sol = Solution()
print(sol.findLeastNumOfUniqueInts([4,3,1,1,3,3,2], 3))
print(sol.findLeastNumOfUniqueInts([5,5,4], 1))
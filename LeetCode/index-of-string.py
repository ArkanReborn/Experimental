class Solution(object):
    # 1 line solution
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
    
    # Second Way to do it
    def secondWay(self, haystack, needle):
        try:
            index = haystack.index(needle)
            return index
        except ValueError:
            return -1
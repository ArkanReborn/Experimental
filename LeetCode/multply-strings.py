class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) * int(num2))

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        dict1 = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        dict2 = {v:k for k, v in dict1.items()}
        n1 = sum([dict1[c] * (10 ** i) for i, c in enumerate(num1[::-1])])
        n2 = sum([dict1[c] * (10 ** i) for i, c in enumerate(num2[::-1])])
        n3, s = n1 * n2, ""
        while n3:
            s = dict2[n3 % 10] + s
            n3 = n3 // 10
        return s if s else "0"

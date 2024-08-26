from fractions import Fraction
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        result = Fraction(0, 1)
        i = 0
        exlen = len(expression)

        while i < exlen:
            sign = 1
            if expression[i] == "-":
                sign = -1
                i += 1
            elif expression[i] == "+":
                i += 1

            j = i
            while j < exlen and expression[j].isdigit():
                j += 1
            numerator = sign * int(expression[i:j])
            i = j + 1
            j = i

            while j < exlen and expression[j].isdigit():
                j += 1
            denominator = int(expression[i:j])

            result += Fraction(numerator, denominator)
            i = j
        return str(result.numerator) + "/" + str(result.denominator)
    
solution = Solution()
print(solution.fractionAddition("-1/2+1/2")) # Output: "0/1"
print(solution.fractionAddition("-1/2+1/2+1/3")) # Output: "1/3"
print(solution.fractionAddition("1/3-1/2")) # Output: "-1/6"
print(solution.fractionAddition("5/3+1/3")) # Output: "12/9"
print(solution.fractionAddition("1/2+2/3")) # Output: "7/6"
print(solution.fractionAddition("5/3+3/4")) # Output: "25/12"

class Solution(object):
    """
    Class representing a solution for sorting people based on their heights.
    """

    def sortPeople(self, names, heights):
        """
        Sorts the given list of names based on the corresponding heights in descending order.

        :param names: A list of strings representing the names of the people.
        :param heights: A list of integers representing the heights of the people.
        :return: A list of strings representing the sorted names.
        """
        sorted_heights = sorted(zip(heights, names), reverse=True)
        res = [n for h, n in sorted_heights]
        return res
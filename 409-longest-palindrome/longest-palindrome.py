class Solution(object):
    def longestPalindrome(self, s):
        count = 0
        odd_found = False

        for char in set(s):
            freq = s.count(char)

            count += (freq // 2) * 2

            if freq % 2 == 1:
                odd_found = True

        if odd_found:
            count += 1

        return count

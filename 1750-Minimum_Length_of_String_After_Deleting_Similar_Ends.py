class Solution(object):
    def minimumLength(self, s):
        i = 0
        j = len(s) - 1

        while i < j and s[i] == s[j]:
            c = s[i]
            while i <= j and s[i] == c:
                i += 1
            while i <= j and s[j] == c:
                j -= 1

        return j - i + 1
        
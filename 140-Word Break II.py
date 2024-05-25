class Solution:
    def wordBreak(self, s, wordDict):
        word_set = set(wordDict)
        return self.wordBreakHelper(s, 0, word_set)
    
    def wordBreakHelper(self, s, start, word_set):
        valid_substr = []
        
        if start == len(s):
            valid_substr.append("")
        for end in range(start + 1, len(s) + 1):
            prefix = s[start:end]
            if prefix in word_set:
                suffixes = self.wordBreakHelper(s, end, word_set)
                for suffix in suffixes:
                    valid_substr.append(prefix + ("" if suffix == "" else " ") + suffix)
        
        return valid_substr
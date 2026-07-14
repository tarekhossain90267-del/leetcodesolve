class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""       
        prefix = strs[0]
        
        for s in strs[1:]:

            while not self.is_prefix(prefix, s):
                prefix = prefix[:-1]
                if not prefix:
                    return ""        
        return prefix
    
    def is_prefix(self, prefix, word):
        if len(prefix) > len(word):
            return False
        for i in range(len(prefix)):
            if prefix[i] != word[i]:
                return False
        return True

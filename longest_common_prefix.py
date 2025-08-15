class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        prefix = strs[0]  # start with first word as prefix
        
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]  # remove last char from prefix
                if not prefix:
                    return ""
        
        return prefix

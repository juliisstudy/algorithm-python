class Solution:
    def lengthOfLongestSubstring(self,s:str) ->int:
        n = len(s)
        ans = 0
        map = {}

        i = 0
        for j in range(n):
            if s[j] in map:
                i = max(map[s[j]],i)
            
            ans = max(ans, j-i+1)
            map[s[j]] = j+1
        return ans
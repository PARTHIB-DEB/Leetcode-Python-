class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs)<2:
            return strs[0]
        strs.sort(key=len)
        i=0
        pref=""
        base_str = strs[0]
        while i<len(base_str):
            s = ""
            for j in range(1,len(strs)):
                if (base_str[i] in strs[j]):
                    if (base_str[i] not in s):
                        s += base_str[i]
                else:
                    s=""
                    break
            pref+=s
            i+=1
        print(pref)
        # return pref
# Solution().longestCommonPrefix(["flower","flow","flight"])
Solution().longestCommonPrefix(["dog","racecar","car"])
        
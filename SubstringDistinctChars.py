class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s)>3:
            good_str_count = 0
            for i in range(len(s)):
                sub_str = s[i:i + 3]
                if len(set(sub_str)) == 3:
                    good_str_count += 1
            return  good_str_count
        elif len(set(s))==3:
            return 1
        else:
            return 0
print(Solution().countGoodSubstrings("xyzzaz"))
print(Solution().countGoodSubstrings("aababcabc"))
class Solution:
    def frequencySort(self, s: str) -> str:
        sorted_s = ""
        letter_count_s = dict()
        for i in set(s):
            letter_count_s[i] = s.count(i)
        letter_count_s_reversed={key: val for key, val in sorted(letter_count_s.items(), key = lambda ele: ele[1], reverse = True)}
        for key,value in letter_count_s_reversed.items():
            sorted_s+=key*value
        return sorted_s
print(Solution().frequencySort("Aabb"))

class Solution:
    def removeDuplicates(self, s: str) -> str:
        old_list = list(s)
        top_value = len(old_list) - 1
        new_list = []

        for i in range(top_value, -1, -1):
            if not new_list or new_list[-1] != old_list[i]:
                new_list.append(old_list[i])
            elif new_list[-1] == old_list[i] :
                new_list.pop()
            old_list.pop()
        new_list = new_list[::-1]
        new_str="".join(new_list)
        return new_str
            
        

print(Solution().removeDuplicates("abbaca"))
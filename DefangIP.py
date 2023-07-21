class Solution:
    def defangIPaddr(self, address: str) -> str:
        str_list=address.split(".")
        new_str="[.]".join(str_list)
        return  new_str


print(Solution().defangIPaddr("1.1.1.1"))
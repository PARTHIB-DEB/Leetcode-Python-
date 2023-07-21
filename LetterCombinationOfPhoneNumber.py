class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits=="":
            return []
        else:
            my_dict = {"abc": 2, "def": 3, "ghi": 4, "jkl": 5, "mno": 6, "pqrs": 7, "tuv": 8, "wxyz": 9}
            Digit_keys = []
            for key, value in my_dict.items():
                if str(value) in digits:
                    Digit_keys.append(key)
            print(Digit_keys)
            count=1
            while(count<=len(Digit_keys[0])):
                row=1
                unit_str=Digit_keys[row][row]
                while(row<=len(Digit_keys)-1):
                    unit_str+=Digit_keys[row]





print(Solution().letterCombinations("23"))
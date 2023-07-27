class Solution(object):
    def isValid(self, s):
        bool_stack = []
        bracket_dict = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for br in s:
            if br in bracket_dict:
                bool_stack.append(br)
            elif len(bool_stack) == 0 or br != bracket_dict[bool_stack.pop()]:
                return False

        return len(bool_stack) == 0
print(Solution().isValid("({{[]}})"))
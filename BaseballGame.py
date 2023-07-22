class Solution:
    def calPoints(self, operations: list[str]) -> int:
        result_stack = []
        for op in operations:
            if op == "C":
                result_stack.pop()
            elif op == "D":
                result_stack.append(result_stack[-1] * 2)
            elif op == "+":
                result_stack.append(result_stack[-1] + result_stack[-2])
            else:
                result_stack.append(int(op))
        return sum(result_stack)

print(Solution().calPoints(["5","2","C","D","+"]))
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        listify_answers=list(answerKey)
        print(listify_answers)
        if listify_answers.count("T") == listify_answers.count("F"):
            if k>=listify_answers.count("T"):
                return len(listify_answers)
            else:
                return len(listify_answers)-k
        else:
            min_value=min(listify_answers.count("T"),listify_answers.count("F"))
            if k>=min_value:
                return len(listify_answers)
            else:
                # return len(listify_answers)-k-min_value Have to think something about this result
            
            
            

print(Solution().maxConsecutiveAnswers(("TTFTTTTTFT"),1))
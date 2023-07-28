class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # My approach
        # listify_answers=list(answerKey)
        # if listify_answers.count("T") == listify_answers.count("F"):
        #     if k>=listify_answers.count("T"):
        #         return len(listify_answers)
        #     else:
        #         return len(listify_answers)-k
        # else:
        #     min_value=min(listify_answers.count("T"),listify_answers.count("F"))
        #     if k>=min_value:
        #         return len(listify_answers)
        #     else:
        #         count=0
        #         if min_value==listify_answers.count("T"):
        #             min_obj="T"
        #             max_obj="F"
        #         else:
        #             min_obj="F"
        #             max_obj="T"
        #         for i in range(len(listify_answers)):
        #             if listify_answers[i]==min_obj:
        #                 listify_answers[i]=max_obj
        #                 min_value=min_value-1
        #             if min_value<1:
        #                 break
        #             else:
                        
        #         for i in listify_answers:
        #             if i==min_obj:
        #                 return count
        #             else:
        #                 count+=1
        l=len(answerKey)
        i=0
        j=0
        t=0
        f=0
        ans=0
        while True:
          while j<l and (t<=k or f<=k):
            if answerKey[j]=='T':
              t+=1
            else:
              f+=1
            j+=1
          if j-i-1>ans:
            ans=j-i-1
          if j==l:
            if (t<=k or f<=k) and j-i>ans:
              ans=j-i
            break
          while i<l and t>k and f>k:
            if answerKey[i]=='T':
              t-=1
            else:
              f-=1
            i+=1
        return ans      
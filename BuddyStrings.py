class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        count = 0  # We have to make count =2 --> True (i!=j)
        s_count_list=[]
        goal_count_list=[]
        for i in range(len(s)):
            if s.count(s[i])>1:
                s_count_list.append(s.count(s[i]))
            if goal.count(goal[i])>1:
                goal_count_list.append(goal.count(goal[i]))
            s_count_list.sort()
            goal_count_list.sort()
        if s_count_list != [] and goal_count_list != [] and s_count_list == goal_count_list:
            return  True
        else:
            for i in range(len(s)):
                for j in range(len(goal)):
                    if i != j and s[i] == goal[j]:
                        count += 1
                return True if count >= 2 else False

print(Solution().buddyStrings("ab","ba"))
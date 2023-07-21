class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        reversed_image=[i[::-1] for i in image]
        for row in reversed_image:
            for col in range(len(row)):
                if int(row[col])==0:
                    row[col]=1
                else:
                    row[col]=0
        return reversed_image



image = [[1,1,0],[1,0,1],[0,0,0]]
print(Solution().flipAndInvertImage(image))
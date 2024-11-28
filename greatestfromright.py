def replaceElements(arr: list[int]) -> list[int]:
        m = -1
        i = len(arr) -1 
        while i >= 0:
            temp = arr[i]
            arr[i] = m
            if temp > m:
                m = temp
            i-= 1
        return arr

print(replaceElements([17,18,5,4,6,1]))
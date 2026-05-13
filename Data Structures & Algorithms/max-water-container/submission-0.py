class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        largest = 0
        while i != j:
            a = min(height[j],height[i])

            if height[j] == height[i]:
                i +=1
                if (a*(j+1-i)) > largest:
                    largest = (a*(j+1-i))
            elif height[j] < height[i]:
                j -=1
                if (a*(j+1-i)) > largest:
                    largest = (a*(j+1-i))
            elif height[j] > height[i]:
                i +=1
                if (a*(j+1-i)) > largest:
                    largest = (a*(j+1-i))
        return largest
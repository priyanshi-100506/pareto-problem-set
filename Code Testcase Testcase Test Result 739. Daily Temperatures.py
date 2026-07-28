class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        stack=[]
        for i,temp in enumerate(temperatures):
            # While the current temperature is warmer than
            # the temperature at the index on the top of the stack,
            # we have found the next warmer day.
            
            while stack and temp>temperatures[stack[-1]]:
                #Get the previous day's index
                prev_index=stack.pop()
                ans[prev_index]=i-prev_index
            stack.append(i)
        return ans

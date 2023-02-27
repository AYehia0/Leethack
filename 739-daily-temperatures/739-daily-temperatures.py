class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        
        # slow O(n**2)
        # ans = [] * len(temps)
        # for ind, temp in enumerate(temps):
        #     days = 0
        #     currTemp = temp
        #     for i in range(ind, len(temps) - 1, 1):
        #         if currTemp < temps[i]:
        #             break
        #         else:
        #             if max(temps[ind:]) == currTemp:
        #                 continue
        #             days += 1
        #     ans.append(days)
        
        # optimized one : O(n) using something really cool called : monotonic stack (dec order)
        ans = [0] * len(temps)
        stack = [] # pairs of temp and current index
        
        for ind, temp in enumerate(temps):
            # the top of the stack (largest value)
            # pop that value and calculate the diff index days
            while stack and temp > stack[-1][0]:
                t, index = stack.pop()
                ans[index] = ind - index
            stack.append((temp, ind))
        return ans
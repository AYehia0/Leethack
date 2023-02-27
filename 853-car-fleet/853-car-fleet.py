class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        The idea behind this problem is kinda hard, but visulizing/drawing the relation between cars speed and postion makes it easier.
        
        Each car can be represented by a linear equation, finding the intersection between lines at the y = target tells if cars will meet before or not.
        
        position
        ^
        |...X <----Target
        |  /
        | /
        |/
        |
        ----------------> time
        Sorting the cars is a good idea since it does matter which comes first or not, and it's easier to find the which car will collide before the other.
        
        """
        # the position and speed pairs
        cars_fleet = [(pos, sp) for pos, sp in zip(position, speed)]
        
        # sorting by position : O(nlogn)
        cars_fleet.sort()
        
        stack = []
        
        # using a stack to add cars, adding the 
        for pos, sp in cars_fleet[::-1]:
            eq = (target - pos) / sp
            stack.append(eq)
            
            # check for collision
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        
        return len(stack)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        po=[[p,s] for p,s in zip(position,speed)]
        po.sort()
        po=po[::-1]
        for p,s in po:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
        
           






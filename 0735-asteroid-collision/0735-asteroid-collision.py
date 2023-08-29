class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            while stack and stack[-1]>0 and i<0:
                if abs(stack[-1])>abs(i):
                    break
                elif abs(stack[-1])<abs(i):
                    stack.pop()
                else:
                    stack.pop()
                    break
            else:
                stack.append(i)
        return stack

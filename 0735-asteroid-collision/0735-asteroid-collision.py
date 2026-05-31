class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for asteroid in asteroids:
            while stack:
                if asteroid < 0 and stack[-1] > 0:
                    if stack[-1] < abs(asteroid):
                        stack.pop()
                        continue
                    elif stack[-1]==abs(asteroid):
                        stack.pop()
                        break
                    else:
                        break
                else:
                    stack.append(asteroid)
                    break
            else:
                stack.append(asteroid)
        return stack 

                    
                





        
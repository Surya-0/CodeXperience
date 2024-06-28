class Solution:
    def asteroidCollision(self, asteroids: 'List[int]') -> 'List[int]':
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                net = a + stack[-1]
                if net < 0:
                    stack.pop()

                elif net > 0:
                    a = 0

                else:
                    stack.pop()
                    a = 0

            if a:
                stack.append(a)

        return stack

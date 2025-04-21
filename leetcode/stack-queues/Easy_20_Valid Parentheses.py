from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        dic = {
            ')': '(',
            '}': '{', 
            ']': '['
        }

        for letter in s:
            if letter in dic.values():
                stack.append(letter)
            elif not stack or stack.pop() != dic[letter]:
                return False
        
        return not stack


            

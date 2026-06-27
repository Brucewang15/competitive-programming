class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest = 0
        i = 0
        while i < len(s):
            stack = []
            k = curStart = i
            while k < len(s):
                if s[k] == '(':
                    stack.append((s[k], k))
                elif s[k] == ')' and not stack:
                    break
                elif s[k] == ')' and stack:
                    stack.pop()
                if not stack:
                    longest = max(longest, k - curStart + 1)
                k += 1

            if len(stack) == 0:
                i = k + 1
            else:
                i = stack[0][1] + 1
                for r in range(1, len(stack), 1):
                    if stack[r-1][1] + 1 != stack[r][1]:
                        break
                    else:
                        i = stack[r][1] + 1
            
        return longest
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # Solution 4
        # Stack stores indexes of boundaries for a substring that ends at index i
        longest = 0
        stack = [-1]

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    longest = max(longest, i - stack[-1])
        return longest

        # Solution 3
        # Bidirectional scan to fix asymmetry. Easier to detect excess ) than (
        stack = 0
        longest = 0
        curStart = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack += 1
            elif s[i] == ')' and stack == 0:
                curStart = i + 1
            elif s[i] == ')':
                stack -= 1
            if stack == 0:
                longest = max(longest, i - curStart + 1)

        stack = 0
        curStart = len(s) - 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ')':
                stack += 1
            elif s[i] == '(' and stack == 0:
                curStart = i - 1
            elif s[i] == '(':
                stack -= 1
            if stack == 0:
                longest = max(longest, curStart - i + 1)
        return longest

        # Solution 2
        # Check for running maximum of longest substring, stopping at first invalid )
        # Then check indexes of left over (
        longest = 0
        stack = []
        curStart = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')' and not stack:
                curStart = i + 1
            elif s[i] == ")" and stack:
                stack.pop()
            if not stack:
                longest = max(longest, i - curStart + 1)
        stack.append(len(s))
        for i in range(1, len(stack), 1):
            longest = max(longest, stack[i] - stack[i-1] - 1)
        return longest

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
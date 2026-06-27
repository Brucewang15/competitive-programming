class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        decoded = ""
        curNumber = 0

        for c in s:
            if c >= 'a' and c <= 'z':
                decoded += c
            elif c.isdigit():
                curNumber = curNumber * 10 + int(c)
            elif c == '[':
                stack.append(decoded)
                stack.append(curNumber)
                curNumber = 0
                decoded = ""
            else: # ]
                prevNum = stack.pop()
                prevDecoded = stack.pop()
                decoded = prevDecoded + prevNum * decoded
        return decoded
    #     decoded, _ = self.decode(s, 0)
    #     return decoded
    # def decode(self, s: str, i: int) -> str:
    #     decoded = ""
    #     curNumber = 0
    #     while (i < len(s)):
    #         if s[i] >= 'a' and s[i] <= 'z':
    #             decoded += s[i]
    #         elif s[i].isdigit():
    #             curNumber = curNumber * 10 + int(s[i])
    #         elif s[i] == '[':
    #             tempDecoded, k = self.decode(s, i+1)
    #             decoded += curNumber * tempDecoded
    #             i = k
    #             curNumber = 0
    #         else: # ]
    #             break
    #         i += 1
    #     return decoded, i
        # decoded = ""
        # stack = []

        # i = 0

        # while i < len(s):
        #     tempdigit=""
        #     tempchars=""

        #     while s[i].isdigit():
        #         tempdigit += s[i]
        #         i+=1
        #     if tempdigit != "" and s[i] == '[':
        #         stack.append(int(tempdigit))
        #         i+=1
        #     while i < len(s) and s[i] >= 'a' and s[i] <= 'z':
        #         tempchars += s[i]
        #         i+=1
        #     if tempchars != "":
        #         stack.append(tempchars)
        #     if i < len(s) and s[i] == ']':
        #         encoded = stack.pop()
        #         k = stack.pop()
        #         if len(stack) == 0:
        #             decoded += k*encoded
        #         else:
        #             stack[-1] += k*encoded
        #         i+=1
        # return decoded

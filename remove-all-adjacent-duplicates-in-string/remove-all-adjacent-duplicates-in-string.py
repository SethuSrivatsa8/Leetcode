class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for c in s:
            if stack and stack[-1]==c:
                while stack and stack[-1]==c:
                    stack.pop()
            else:
                stack.append(c)
        res="".join(stack)
        return res 
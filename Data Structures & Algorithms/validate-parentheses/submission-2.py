class Solution:
    def isValid(self, s: str) -> bool:
        # notice the FIFO ordering. If the opening bracket is first, it's corresponding closing bracket must be firs
        stack = []
        match = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for bracket in s:
            if bracket == '(' or bracket == '{' or bracket == '[':
                stack.append(match[bracket])
            else:
                if not stack or stack.pop() != bracket:
                    return False
        return len(stack) == 0
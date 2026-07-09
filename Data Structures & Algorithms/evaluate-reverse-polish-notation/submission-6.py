class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stack = []
        for token in tokens:
            match token:
                case "+":
                    r = stack.pop()  
                    l = stack.pop()
                    stack.append(l + r)
                case "-":
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(l - r)
                case "*": 
                    r = stack.pop()
                    l = stack.pop()
                    stack.append(l * r)
                case "/":
                    r = stack.pop()
                    l = stack.pop()
                    if r == 0:
                        return 0
                    stack.append(int(l / r))
                case _:
                    stack.append(int(token))
        return stack[0]

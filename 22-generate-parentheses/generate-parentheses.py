class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        resArr = []
        stack = []

        def dfs(openN, closedN):
            if openN == closedN == n:
                temp_stack = "".join(stack)
                resArr.append(temp_stack)
                return 
            
            # Add open bracket
            if openN < n:
                stack.append("(")
                dfs(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                dfs(openN, closedN + 1)
                stack.pop()
        
        dfs(0,0)
        return resArr



        

























class Solution:
    def reverseParentheses(self, s):
        ind_stack= deque()
        res = []

        for char in s:
            if char == "(":  # start new string we need to reverse first
                ind_stack.append(len(res))  # string starts on next index
            elif char == ")":  # reverse string from last added start index
                start_ind= ind_stack.pop()
                res[start_ind:] = res[start_ind:][::-1]
            else:
                res.append(char)

        return "".join(res)
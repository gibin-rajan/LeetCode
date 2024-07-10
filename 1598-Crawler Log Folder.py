class Solution:
    def minOperations(self, logs):
        paths_stack = []

        for log in logs:
            if log == "../":
                if paths_stack:
                    paths_stack.pop()
            elif log != "./":
                paths_stack.append(log)

        return len(paths_stack)
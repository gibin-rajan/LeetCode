class Solution:
    def grayCode(self, n: int) -> List[int]:
        def dfs(path):
            # action
            if len(path) == n:
                return [path]

            # continue path with 0 first
            a = dfs(path + '0')

            # then continue path with 1
            b = dfs(path + '1')

            # reverse the order of possibilities for 1 case
            b = b[::-1]

            # append 0 and 1 lists
            return a + b

        # base
        if n == 0:
            return [0]

        res =  dfs('')
        
        # map path string to integers
        return list(map(lambda x: int(x, 2), res))
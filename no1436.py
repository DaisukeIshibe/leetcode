class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        pair = paths.pop(0)
        if paths == []:
            return pair[-1]
        else:
            p_dict: dict = {}
            for start, end in paths:
                if not start in p_dict:
                    p_dict[start] = end
            
            while True:
                _, curr_end = pair
                if curr_end in p_dict:
                    pair = [curr_end, p_dict[curr_end]]
                    del p_dict[curr_end]
                else:
                    break

            return pair[-1]


sol = Solution()
paths = [["B","C"],["D","B"],["C","A"]]
print(f'{sol.destCity(paths)} expect A')
paths = [["A","Z"]]
print(f'{sol.destCity(paths)} expect Z')
paths = [["A","B"],["C","Y"],["B","D"],["D","C"],["Y","Z"]]
print(f'{sol.destCity(paths)} expect Z')
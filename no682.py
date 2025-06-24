class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack_list = []
        for op in operations:
            if op == 'C':
                stack_list.pop(-1)
            elif op == 'D':
                a = int(stack_list[-1])
                stack_list.append(a * 2)
            elif op == '+':
                a = int(stack_list[-1])
                b = int(stack_list[-2])
                stack_list.append(a + b)
            else:
                stack_list.append(int(op))
        
        return sum(stack_list)

sol = Solution()
print(f'{sol.calPoints(["5","2","C","D","+"])} Expect 30')
print(f'{sol.calPoints(["5","-2","4","C","D","9","+","+"])} Expect 27')
print(f'{sol.calPoints(["1","C"])} Expect 0')
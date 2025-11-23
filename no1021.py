class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        len_s = len(s)
        stack_list = []
        for i in range(len_s):
            c = s[i]
            if stack_list == []:
                stack_list.append(c)
            elif (stack_list[-1] == '(') and (c == ')'):
                print('find ()')
                stack_list.pop(-1)

        return

sol = Solution()
s = "(()())(())"
ans = "()()()"
if sol.removeOuterParentheses(s) == ans:
    print('no1 OK')
else:
    print('no1 NG')

s = "(()())(())(()(()))"
ans = "()()()()(())"
if sol.removeOuterParentheses(s) == ans:
    print('no2 OK')
else:
    print('no2 NG')

s = "()()"
ans = ""
if sol.removeOuterParentheses(s) == ans:
    print('no3 OK')
else:
    print('no3 NG')

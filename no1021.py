class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        s_ = s.replace('((','(')
        s_ = s_.replace('))',')')
        if s == s_:
            return ''
        else:
            print(s_)
            return s_

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

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        t_list = [s for s in sorted(letters) if s > target]
        if t_list == []:
            return letters[0]
        else:
            return  t_list[0]

sol = Solution()
print(f'{sol.nextGreatestLetter(["c", "f", "j"], "a")} expect c')
print(f'{sol.nextGreatestLetter(["c","f","j"], "c")} expect f')
print(f'{sol.nextGreatestLetter(["x","x","y","y"], "z")} expect x')
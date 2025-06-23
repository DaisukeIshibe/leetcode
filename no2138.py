class Solution:
    def split_list(self, input_list, n):
        for idx in range(0, len(input_list), n):
            yield input_list[idx:idx+n]

    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        split_list = list(self.split_list(s, k))
        last_element = split_list[-1]
        last_len = len(last_element)
        if last_len != k:
            for _ in range(k - last_len):
                split_list[-1] += fill
        return split_list

sol = Solution()
s = "abcdefghi"
k = 3
fill = "x"
print(f'{s} {k} {fill}->{sol.divideString(s, k, fill)} expect {["abc","def","ghi"]}')
s = "abcdefghij"
k = 3
fill = "x"
print(f'{s} {k} {fill}->{sol.divideString(s, k, fill)} expect {["abc","def","ghi","jxx"]}')
s = "ctoyjrwtngqwt"
k = 8
fill = "n"
print(f'{s} {k} {fill}->{sol.divideString(s, k, fill)} expect {["ctoyjrwt","ngqwtnnn"]}')

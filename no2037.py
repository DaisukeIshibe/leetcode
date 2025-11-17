class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        sum_seat = sum(seats)
        sum_stud = sum(students)
        print(f'{sum_seat} {sum_stud}')
        return abs(sum_seat - sum_stud)

sol = Solution()
print(f'{sol.minMovesToSeat([3,1,5], [2,7,4])} expect 4')
print(f'{sol.minMovesToSeat([4,1,5,9], [1,3,2,6])} expect 7')
print(f'{sol.minMovesToSeat([2,2,6,6], [1,3,2,6])} expect 4')
print(f'{sol.minMovesToSeat([12,14,19,19,12], [19,2,17,20,7])} expect 19')
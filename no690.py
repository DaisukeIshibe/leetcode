from typing import List
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_map = {employee.id: employee for employee in employees}
        total_importance = 0
        stack = [employee_map[id]]

        while stack:
            current_employee = stack.pop()
            total_importance += current_employee.importance
            for subordinate_id in current_employee.subordinates:
                stack.append(employee_map[subordinate_id])

        return total_importance
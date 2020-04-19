from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:

    # 690 Employee Importance
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        dic = {e[0]:e[1:] for e in employees}
        print(dic)
        def dfs(id):
            employee = dic[id]
        pass

if __name__ == '__main__':
    s =Solution()
    n, id = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
    s.getImportance(n, id )
    
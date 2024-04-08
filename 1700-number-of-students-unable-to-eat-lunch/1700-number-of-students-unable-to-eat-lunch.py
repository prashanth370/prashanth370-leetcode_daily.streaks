from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque(students)
        for sandwich in sandwiches:
            if sandwich in queue:
                queue.rotate(-queue.index(sandwich))
                queue.popleft()
            else:
                break
        return len(queue)

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentCounter = Counter(students)
        for s in sandwiches:
            if studentCounter[s] > 0:
                studentCounter[s] -= 1
            else:
                return studentCounter.total()

        return 0

from base_test_spec import BaseTestSpec
from base_problem_spec import BaseProblemSpec

class ProblemSpec(BaseProblemSpec):
    def __init__(self, A: int, B: int) -> None:
        super().__init__()
        self.A = A
        self.B = B

    def InputFormat(self):
        self.LINE(self.A, self.B)

    def Constraints(self):
        self.CONS(1 <= self.A <= 5)

    def Subtask1(self):
        self.CONS(1 <= self.B <= 10)

    def Subtask2(self):
        self.CONS(1 <= self.B <= 100)

class TestSpec(BaseTestSpec):

    def TestCases(self):
        self.CASE(ProblemSpec(
            A=5,
            B=500
        ))

    def TestGroup1(self):
        self.Subtasks({2})
        self.CASE(ProblemSpec(
            A=4,
            B=100
        ))

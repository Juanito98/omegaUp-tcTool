from src.base_test_spec import BaseTestSpec
from src.base_problem_spec import BaseProblemSpec


class ProblemSpec(BaseProblemSpec):
    def __init__(self, A: int, B: int) -> None:
        super().__init__()
        self.A = A
        self.B = B

    def InputFormat(self) -> None:
        self.LINE(self.A, self.B)

    def Constraints(self) -> None:
        self.CONS(1 <= self.A <= 5)

    def Subtask1(self) -> None:
        self.CONS(1 <= self.B <= 10)

    def Subtask2(self) -> None:
        self.CONS(1 <= self.B <= 100)


class TestSpec(BaseTestSpec):

    def SampleTestCases(self) -> None:
        self.CASE(ProblemSpec(A=1, B=2))
        self.CASE(ProblemSpec(A=3, B=3))

    def TestCases(self) -> None:
        self.CASE(ProblemSpec(A=5, B=500))
        self.CASE(ProblemSpec(A=2,B=100))

    def TestGroup1(self) -> None:
        self.Subtasks({2})
        self.CASE(ProblemSpec(A=4,B=100))

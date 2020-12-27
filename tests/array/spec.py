from typing import Sequence
from src.base_test_spec import BaseTestSpec
from src.base_problem_spec import BaseProblemSpec

import random

def eachElementBetween(A, lo, hi):
    for x in A:
        if x < lo or x > hi:
            return False
    return True

class ProblemSpec(BaseProblemSpec):
    N : int
    A : Sequence[int]

    def __init__(self, N : int, A : Sequence[int]) -> None:
        super().__init__()
        self.N = N
        self.A = A

    def InputFormat(self) -> None:
        self.LINE(self.N)
        self.LINE(*self.A)

    def Constraints(self) -> None:
        self.CONS(2 <= self.N <= 100000)
        self.CONS(eachElementBetween(self.A, -100000, 100000))


class TestSpec(BaseTestSpec):

    def SampleTestCases(self) -> None:
        self.CASE(ProblemSpec(N = 4, A = [4, -2, 3, 1]))

    def TestCases(self) -> None:
        self.CASE(ProblemSpec(N = 5, A = [-2, -1, 2, 3, 0]))
        self.CASE(ProblemSpec(N=5, A=[3, 4, -1, -3, -5]))
        self.CASE(ProblemSpec(N=2, A=[2, -1]))
        self.CASE(ProblemSpec(N=100000, A=[random.randint(-10, 10) for i in range(100000)]))

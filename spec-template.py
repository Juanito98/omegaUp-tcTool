from src.base_test_spec import BaseTestSpec
from src.base_problem_spec import BaseProblemSpec


class ProblemSpec(BaseProblemSpec):
    def __init__(self) -> None:
        super().__init__()
        """Declare variables here"""

    def InputFormat(self) -> None:
        """Set input format"""

    def Constraints(self) -> None:
        """Define Constrains for problem"""


class TestSpec(BaseTestSpec):

    def SampleTestCases(self) -> None:
        """Add here sample test cases"""
        pass

    def TestCases(self) -> None:
        """Add here official test cases"""
        pass
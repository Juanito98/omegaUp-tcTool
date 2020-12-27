from io_formatter import IOFormatter
import unittest


class BaseProblemSpec(unittest.TestCase, IOFormatter):
    def __init__(self) -> None:
        super().__init__()
        self.subtasks = [
            self.Subtask1,
            self.Subtask2,
            self.Subtask3
        ]
    

    def CONS(self, predicate: bool) -> None:
        self.assertTrue(predicate)

    def InputFormat(self): pass
    def Constraints(self): pass
    def Subtask1(self): pass
    def Subtask2(self): pass
    def Subtask3(self): pass
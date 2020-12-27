from src.io_formatter import IOFormatter
import unittest


class BaseProblemSpec(unittest.TestCase, IOFormatter):
    subtasks = []

    def __init__(self) -> None:
        super().__init__()
        self.subtasks = [
            self.Subtask1,
            self.Subtask2,
            self.Subtask3,
            self.Subtask4,
            self.Subtask5,
            self.Subtask6,
            self.Subtask7,
            self.Subtask8,
            self.Subtask9,
            self.Subtask10
        ]

    def CONS(self, predicate: bool) -> None:
        self.assertTrue(predicate)

    def InputFormat(self): pass
    def Constraints(self): pass
    def Subtask1(self): pass
    def Subtask2(self): pass
    def Subtask3(self): pass
    def Subtask4(self): pass
    def Subtask5(self): pass
    def Subtask6(self): pass
    def Subtask7(self): pass
    def Subtask8(self): pass
    def Subtask9(self): pass
    def Subtask10(self): pass

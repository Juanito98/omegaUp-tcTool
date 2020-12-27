from src.base_problem_spec import BaseProblemSpec
import os


class BaseTestSpec:
    officialTestCasePath: str = None
    sampleTestCasePath: str = None
    testGroups = []

    _currStdinPath: str = None
    _currFileName: str = None
    _currSubtasks = {}
    _currCaseNum: int = 0

    def __init__(self) -> None:
        super().__init__()
        self._testGroups = [
            self.TestGroup1,
            self.TestGroup2,
            self.TestGroup3,
            self.TestGroup4,
            self.TestGroup5,
            self.TestGroup6,
            self.TestGroup7,
            self.TestGroup8,
            self.TestGroup9,
            self.TestGroup10,
        ]

    def CASE(self, problemSpec: BaseProblemSpec) -> None:
        if not os.path.exists(self._currStdinPath):
            os.makedirs(self._currStdinPath)
        self._currCaseNum += 1
        with open(self._currStdinPath + "/" + self._currFileName + "{}.in".format(self._currCaseNum), "w") as f:
            problemSpec.setInputFile(f)
            problemSpec.Constraints()
            for subtask_id in self._currSubtasks:
                problemSpec.subtasks[subtask_id-1]()
            problemSpec.InputFormat()

    def setOfficialTestCasePath(self, officialTestCasePath: str) -> None:
        self.officialTestCasePath = officialTestCasePath

    def setSampleTestCasePath(self, sampleTestCasePath: str) -> None:
        self.sampleTestCasePath = sampleTestCasePath

    def _preGeneration(self, stdinPath: str, filenamePref: str):
        self._currStdinPath = stdinPath
        self._currFileName = filenamePref
        self._currSubtasks = {}
        self._currCaseNum = 0

    def Subtasks(self, subtasks) -> None:
        self._currSubtasks = subtasks

    @staticmethod
    def generateInputs(testSpec: 'BaseTestSpec', officialTestCasePath: str, sampleTestCasePath: str = None) -> None:
        testSpec.setOfficialTestCasePath(officialTestCasePath)
        testSpec.setSampleTestCasePath(sampleTestCasePath)

        # Generating official test cases
        testSpec._currStdinPath = testSpec.officialTestCasePath
        # Generate test groups
        for i in range(len(testSpec._testGroups)):
            testSpec._preGeneration(officialTestCasePath, 'g' + str(i+1) + '.')
            testSpec._testGroups[i]()
        # Generate testCases
        testSpec._preGeneration(officialTestCasePath, 'case')
        testSpec.TestCases()

        # Generating sample test cases
        testSpec._preGeneration(sampleTestCasePath, 'sample')
        testSpec.SampleTestCases()

    def TestCases(self) -> None: pass
    def TestGroup1(self) -> None: pass
    def TestGroup2(self) -> None: pass
    def TestGroup3(self) -> None: pass
    def TestGroup4(self) -> None: pass
    def TestGroup5(self) -> None: pass
    def TestGroup6(self) -> None: pass
    def TestGroup7(self) -> None: pass
    def TestGroup8(self) -> None: pass
    def TestGroup9(self) -> None: pass
    def TestGroup10(self) -> None: pass

    def SampleTestCases(self) -> None: pass

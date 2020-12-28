from src.base_test_spec import BaseTestSpec

def generateInputs(testSpec: BaseTestSpec, officialTestCasePath: str, sampleTestCasePath) -> None:
    BaseTestSpec.generateInputs(
        testSpec, officialTestCasePath, sampleTestCasePath)

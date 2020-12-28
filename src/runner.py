from src.base_test_spec import BaseTestSpec
import importlib.util

def generateInputs(specPath: str, officialTestCasePath: str, sampleTestCasePath: str) -> None:
    spec = importlib.util.spec_from_file_location(
        "TestSpec", specPath)
    specModule = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(specModule)
    testSpec = specModule.TestSpec()

    BaseTestSpec.generateInputs(
        testSpec, officialTestCasePath, sampleTestCasePath)

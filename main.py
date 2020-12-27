import os
import problems
import importlib.util
import src.runner

rootDirectory = problems.repositoryRoot()

for p in problems.problems(allProblems=True,
                           rootDirectory=rootDirectory,
                           problemPaths=[]):
    specPath = os.path.join(rootDirectory, p.path, 'spec.py')
    casesPath = os.path.join(rootDirectory, p.path, 'cases')
    examplePath = os.path.join(rootDirectory, p.path, 'examples')

    spec = importlib.util.spec_from_file_location(
        "TestSpec", specPath)
    specModule = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(specModule)
    testSpec = specModule.TestSpec()
    src.runner.generateInputs(testSpec, casesPath, examplePath)
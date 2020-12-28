import os
import problems
import src.runner

rootDirectory = problems.repositoryRoot()

for p in problems.problems(allProblems=True,
                           rootDirectory=rootDirectory,
                           problemPaths=[]):
    specPath = os.path.join(rootDirectory, p.path, 'spec.py')
    casesPath = os.path.join(rootDirectory, p.path, 'cases')
    examplePath = os.path.join(rootDirectory, p.path, 'examples')

    src.runner.generateInputs(specPath, casesPath, examplePath)
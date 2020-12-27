from base_problem_spec import BaseProblemSpec

class BaseTestSpec:
    def __init__(self) -> None:
        super().__init__()
        self._currSubtasks = {}

    def CASE(self, problemSpec: BaseProblemSpec) -> None:
        problemSpec.Constraints()
        for subtask_id in self._currSubtasks:
            problemSpec.subtasks[subtask_id-1]()
        problemSpec.InputFormat()

    def Subtasks(self, subtasks) -> None:
        self._currSubtasks = subtasks
from typing import Sequence
from src.base_test_spec import BaseTestSpec
from src.base_problem_spec import BaseProblemSpec

def eachElementBetween(A, lo, hi):
    for x in A:
        if x < lo or x > hi:
            return False
    return True


def noSelfLoop(U, V):
    for i in range(len(U)):
        if U[i] == V[i]:
            return False
    return True

def isConnected(n, U, V):
    visited = [False] * n
    adj = {i : [] for i in range(n)}
    for i in range(len(U)):
        adj[U[i]] += [V[i]]
        adj[V[i]] += [U[i]]
    nodesVisited = 0
    p = [0]
    while len(p) > 0:
        nodo = p.pop()
        if visited[nodo]:
            continue
        visited[nodo] = True
        nodesVisited += 1
        for u in adj[nodo]:
            p += [u]
    return nodesVisited == n

class ProblemSpec(BaseProblemSpec):
    def __init__(self,
                 N: int,
                 M: int,
                 U: Sequence[int],
                 V: Sequence[int],
                 W: Sequence[int]) -> None:
        super().__init__()
        self.N = N
        self.M = M
        self.U = U
        self.V = V
        self.W = W

    def InputFormat(self) -> None:
        self.LINE(self.N, self.M)
        self.LINES(self.U, self.V, self.W)

    def Constraints(self) -> None:
        self.CONS(2 <= self.N <= 100000)
        self.CONS(self.N-1 <= self.M <= 100000)
        self.CONS(eachElementBetween(self.U, 0, self.N - 1))
        self.CONS(eachElementBetween(self.V, 0, self.N - 1))
        self.CONS(eachElementBetween(self.W, 1, 1000))
        self.CONS(noSelfLoop(self.U, self.V))
        self.CONS(isConnected(self.N, self.U, self.V))


class TestSpec(BaseTestSpec):

    def SampleTestCases(self) -> None:
        self.CASE(ProblemSpec(
            N = 3, M = 3,
            U = [0, 1, 2],
            V = [1, 2, 0],
            W = [2, 3, 4]
        ))

    def TestCases(self) -> None:
        """Add here official test cases"""
        self.CASE(ProblemSpec(
            N=2, M=1, U=[0], V=[1], W=[1]
        ))

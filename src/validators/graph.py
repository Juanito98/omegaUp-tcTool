from typing import Sequence


def noSelfLoop(U: Sequence[int], V: Sequence[int]) -> bool:
    for i in range(len(U)):
        if U[i] == V[i]:
            return False
    return True


def isConnected(n: int, U: Sequence[int], V: Sequence[int]) -> bool:
    visited = [False] * n
    adj = {i: [] for i in range(n)}
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

from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.adjacentNodes = []


def depthFirst(startingNode, soughtValue):
    visitedNodes = set()
    stack = [startingNode]

    while len(stack) > 0:
        node = stack.pop()
        if node in visitedNodes:
            continue

        visitedNodes.add(node)
        if node.value == soughtValue:
            return True

        for n in node.adjacentNodes:
            if n not in visitedNodes:
                stack.append(n)
    return False


def breadthFirst(startingNode, soughtValue):
    visitedNodes = set()
    queue = deque([startingNode])

    while len(queue) > 0:
        node = queue.pop()
        if node in visitedNodes:
            continue

        visitedNodes.add(node)
        if node.value == soughtValue:
            return True

        for n in node.adjacentNodes:
            if n not in visitedNodes:
                queue.appendleft(n)
    return False


# a = set()
# a.add(6)
# print(a, type(a))
N = [
    {b, c, d, e, f},
    {c, e},
    {d},
    {e},
    {f},
    {c, g, h},
    {f, h},
    {f, g}
]
depthFirst(G, 'A')
# while True:
#     if 5 > 0: continue
#     print("s")

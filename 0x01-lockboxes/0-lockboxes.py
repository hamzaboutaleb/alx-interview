#!/usr/bin/python3
""" Lockboxes """


def dfs(boxes, node, visited):
    """depth first search
    Args:
      boxes: list of all boxies
      node: current box
      visited: set contains all visited nodes
    """
    if node in visited:
        return
    visited.add(node)
    for box in boxes[node]:
        if box not in visited:
            dfs(boxes, box, visited)


def canUnlockAll(boxes):
    """lockboxes solution
    Args:
      boxes: list of boxes
    Returns:
      True if all boxes can be opened, else return False
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True
    visited = set()
    dfs(boxes, 0, visited)
    if (len(visited) == len(boxes)):
        return True
    return False

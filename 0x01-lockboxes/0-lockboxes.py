#!/usr/bin/python3
""" Lockboxes """


def dfs(boxes, node, visited):
    """depth first search
    Args:
      boxes: list of all boxies
      node: current box
      visited: set contains all visited nodes
    """
    stack = [0]
    
    while len(stack) > 0:
        current = stack.pop()
        visited.add(current)
        if current >= len(boxes):
            continue
        for box in boxes[current]:
            if box not in visited:
                stack.append(box)
    if len(visited) == len(boxes):
        return True
    else:
        return False


def canUnlockAll(boxes):
    """lockboxes solution
    Args:
      boxes: list of boxes
    Returns:
      True if all boxes can be opened, else return False
    """
    if len(boxes) == 0 or boxes == [[]]:
        return True
    visited = set()
    return dfs(boxes, 0, visited)

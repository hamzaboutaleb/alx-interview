#!/usr/bin/python3
def dfs(boxes, node, visited):
  if node in visited:
    return
  visited.add(node)
  for box in boxes[node]:
    if box not in visited:
      dfs(boxes, box, visited)

def canUnlockAll(boxes):
  if (len(boxes) == 0):
    return True
  visited = set()
  dfs(boxes, 0, visited)
  if (len(visited) == len(boxes)):
    return True
  return False

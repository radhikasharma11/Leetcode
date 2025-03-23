from collections import deque
#graph = {1: [2,3,4], 2:[1,5], 3:[1,6,7], 4:[1,8], 5:[2],6:[3,9],7:[3],8:[4], 9:[6]}
graph = {"A":["B","C", "D"],
           "B":["E"],
           "C":["F","G"],
           "D":["H"],
           "E":["I"],
           "F":["J"]}

# Queue
def bfs(graph, head):
    root = head
    bfs_traversal = []
    queue = deque([root])
    while queue:
        head = queue.popleft()
        bfs_traversal.append(head)
        if head not in graph:
            continue
        for g in graph[head]:
            queue.append(g)
            #graph[g].remove(head)

    print(bfs_traversal)

#bfs(graph, "A")

#Stack operation + recursion
dfs_traversal = []
def dfs(graph, head):
    root = head
    dfs_traversal.append(root)
    stack = [root]
    while stack:
        head = stack.pop()
        if head not in graph:
            return
        for g in graph[head]:
            #graph[g].remove(head)
            dfs(graph, g)



dfs(graph, "A")
print(dfs_traversal)

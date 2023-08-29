#Rev linked list

def f(h):
    curr = h
    prev = None

    while curr:
        n_next = curr.next
        curr.next = prev
        prev = curr
        curr = n_next

    return prev

#Monotonic increasing stack(same logic for monotonic queue)

def f(a):
    s = []
    z = 0

    for i in a:
        # For monotonic decreasing flip sign
        while(stack and stack[-1] > i):
            # logic
            s.pop()
        s.append(i)

    return z

# DFS Traversal(recursive)

def dfs_r(root):
    if not root: return

    z = 0

    dfs_r(root.left)
    dfs_r(root.right)

    return z

# DFS Traversal(iterative)

def dfs_i(root):
    if not root: return

    s = [root]; z = 0 

    while s:
        curr = s.pop()

        if(curr.left): s.append(curr.left)
        if(curr.right): s.append(curr.right)

   return z 

# BFS Traversal(binary tree)

def bfs(node, t):

    q = deque([node]); z = 0

    while q:

        n = len(q)

        for _ in n:
            curr = q.popleft()

            if(curr.left): q.append(curr.left)
            if(curr.right): q.append(curr.right)

    return z

# DFS Graph Traversal(recursive)

def f(graph):

    seen = set()

    def dfs_gr(node):

        z = 0

        for adj in graph[node]:
            if(adj not in seen):
                seen.add(adj)
                ans += dfs_gr(adj)

        return z

    return dfs_gr(start_node)


# DFS Graph Traversal(iterative)

def dfs_gi(graph):

    s = [start_node]
    seen = set()
    z = 0

    while s:
        curr_node = s.pop()

        for adj in graph[curr_node]:
            if(adj not in seen):
                seen.add(adj)
                s.append(adj)

    return z


# Dynamic programming 

def fn(a):

    memo = [SOME_SIZE]

    def dp(state):

        if(base_case): return 0
        if(memo[state]): return memo[state]

        z = recurrance_relation(state)
        memo[state] = z
        
        return z

    return(dp(whole_input_state))


# Backtracking

def backtrack(curr, other_args, ...):

    if(base_case):
        # modify answer
        return

    z = 0

    for i in interate_over_state:
        # modfiy state
        z += backtrack(i, other_args, ...)
        # undo modification

    return z











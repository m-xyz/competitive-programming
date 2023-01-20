## Backtracking

Backtracking is a general algorithm for finding all(or some) solutions to some computational problems(notably Constraint satisfaction problems or CSPs), which incrementally builds candidates to the solution and abandons a candidate ('backtracks') as soon as it determines that the candidate cannot lead to a valid solution.

Similiar to how we would traverse a tree, starting at the root node we set out to find the solutions located at leaf nodes. Each intermediate node represents a partial candidate to the solution that COULD leads us to the final solution. At each candidate node we branch out to its children, once we determine that the current node isn't going to lead to the final solution, we backtrack to its parent to explore other possibilities. This leads to a much more efficient brute force algorithm.

NOTE: There's a common pattern in backtracking algorithms:
    1. Make a choice
    2. Check if choice is valid given the problem's constraints:
        2.1 If it's valid, keep exploring this path, until we either reach a solution or a choice that isn't valid.
        2.2 If it's not valid go to step 3.
    3. Undo choice.

A classical applicattion of backtracking is the famous N_Queens problem, the problem description goes as follow:

    - Given an N x N chessboard, count the number of ways one can place N queens, such that no queens is attacking another queen.

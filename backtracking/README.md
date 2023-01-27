## Backtracking

Backtracking is a general algorithm for finding all(or some) solutions to some computational problems(notably Constraint satisfaction problems or CSPs), which incrementally builds candidates to the solution and abandons a candidate ('backtracks') as soon as it determines that the candidate cannot lead to a valid solution. Why? Say we are at candidate i, we iterate over children[i], and check if any are within the constraints defined for the problem, if they aren't there's no need to try and branching out that children, doing so allows us to prune the search zone.

Similiar to how we would traverse a tree, starting at the root node we set out to find the solutions located at leaf nodes. Each intermediate node represents a partial candidate to the solution that COULD leads us to the final solution. At each candidate node we branch out to its children, once we determine that the current node isn't going to lead to the final solution, we backtrack to its parent to explore other possibilities. This leads to a much more efficient brute force algorithm.

![](https://github.com/m-xyz/AOC_2022/blob/main/backtracking/backtracking.png)</br>


NOTE: There's a common pattern in backtracking algorithms:</br>
    1. Make a choice</br>
    2. Check if choice is valid given the problem's constraints:</br>
        2.1 If it's valid, keep exploring this path, until we either reach a solution or a choice that isn't valid.</br>
        2.2 If it's not valid go to step 3.</br>
    3. Undo choice.</br>

A general template for backtracking would be:

```python
    def backtrack(candidate):
        if find_solution(candidate):
            output(candidate)
            return

        # Iterate over all possible candidates
        for next_candidate in possible_candidates:
            if is_valid(next_candidate):

                #Try this partial candidate's solution
                place(next_candidate)

                #Give this candidate, let's explore further down this path
                backtrack(next_candidate)

                #Backtrack
                remove(next_candidate)
```

A classical application of backtracking is the famous N_Queens problem, the problem description goes as follow</br>
Given an N x N chessboard, count the number of ways one can place N queens, such that no queens is attacking another queen.</br>
![](https://github.com/m-xyz/AOC_2022/blob/main/backtracking/n_queen_constraints.png)</br>

Solving N_Queens using backtracking:
    1. Iterate over each row of the board, if we ever get to the final cell(board[N-1][N-1]) that means a solutions was found.</br>
    2. Once we are at row $R_x$, we iterate over each column $C_y$, we then consider placing a queen at board[$R_x$][$C_y$], in provided code
    there's 3 lookup tabels, col, diag1 and diag2, meaning $Column_i$, $PositiveDiagonal_i$ and $NegativeDiagonal_i$, which store if there is currently
    a queen placed at a given column and respective diagonals.

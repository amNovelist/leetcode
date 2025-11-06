"""
Source: https://www.geeksforgeeks.org/dsa/introduction-to-backtracking-2/

Backtracking is a problem-solving algorithmic technique that involves finding a solution incrementally by trying different options and undoing them if they lead to a dead end.

Backtracking is used to explore multiple possibilities in problems such as finding a path in a maze or solving puzzles like Sudoku, by systematically trying different choices.
When a choice leads to a dead end, the algorithm backtracks to the previous decision point and tries a different path, avoiding unnecessary exploration of invalid solutions.
frame_3105
How does Backtracking work?
Backtracking is a systematic trial-and-error technique where we build a solution step by step and undo (or “backtrack”) whenever we hit a dead end.

The idea is simple:

Choose – Start by making a choice that could lead toward a solution.
Explore – Recursively move forward with this choice.
Check validity – If the choice leads to an invalid state, undo it (backtrack) and try another option.
Repeat – Continue this process until all possibilities are explored or a valid solution is found.
Backtracking ensures we don’t waste time pursuing impossible paths. Instead, it systematically explores only feasible ones by backing up whenever a choice fails.

Example - N Queens Problem
In the N-Queens problem, the goal is to place N queens on an N×N chessboard so that no two queens attack each other.

Choose: Start with the first row and try placing a queen in one column.
Explore: Move to the next row and attempt placing a queen in a safe column.
Check validity: If the placement causes conflict (same column, diagonal clash), that branch is invalid backtrack and try the next column.
Repeat: Continue row by row, placing queens only in safe positions.
Success: If queens are placed in all rows without conflict, we found a valid solution.
the_knight_s_tour_problem_8
Without backtracking, we would have to test all possible arrangements of queens (which grows exponentially). Most of these arrangements are invalid because queens attack each other. By checking validity at every step (no two queens in the same column or diagonal), backtracking saves time by stopping early whenever a partial placement becomes invalid, ensuring we only explore feasible board states.


When to Use Backtracking
Constraint satisfaction problems: When you need to build a solution step by step and must satisfy certain conditions (e.g., N-Queens, Sudoku, Rat in a Maze).
Search problems: When the solution space is large, but invalid or infeasible branches can be pruned early.
Multiple solutions: When you need to explore all possible valid solutions, not just one.
Combinatorial problems: When you must generate all valid combinations, permutations, or subsets under constraints.

When Not to Use Backtracking
Greedy or DP fits better: If the problem can be solved directly using a greedy strategy or dynamic programming, backtracking is overkill.
No pruning possible: If all branches must be explored anyway (no constraints to cut early), brute force or iterative methods may be simpler.
Large input size: Backtracking can be exponential in time. For very large inputs without strong pruning opportunities, it becomes impractical.
Single optimal solution: If the task only needs one best solution with clear optimization criteria, algorithms like DP, greedy, or graph search may be faster.


Standard Backtracking Problems
N-Queen Problem
Solve Sudoku
M-coloring problem
Rat in a Maze
The Knight's tour problem
Permutation of given String
For more practice problems: click here


"""
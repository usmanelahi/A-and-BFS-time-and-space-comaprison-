from time import time
from BFS_search import breadth_first_search
from Astar_search import Astar_search
from puzzle import Puzzle


state=[[1, 3, 4,
        8, 6, 2,
        7, 0, 5],

       [2, 8, 1,
        0, 4, 3,
        7, 6, 5],

       [2, 8, 1,
        4, 6, 3,
        0, 7, 5]]

for i in range(0,3):
    Puzzle.num_of_instances=0
    t0=time()
    bfs=breadth_first_search(state[i])
    t1=time()-t0
    print('BFS:', bfs)
    print('space calculation for bfs:', Puzzle.num_of_instances)
    print('time taken by bfs:', t1)
    print()

    print('------------------------------------------')
    print()

    
    Puzzle.num_of_instances = 0
    t0 = time()
    astar = Astar_search(state[i])
    t1 = time() - t0
    print('A*:', astar)
    print('space calculation for A*:', Puzzle.num_of_instances)
    print('time taken by A*:', t1)
    print()

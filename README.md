# Priority Queue For A* Search
Anyone of you can use this package to handle the priority Queue part of your A* Search code.
[PyPi Link](https://pypi.org/project/prioQbyrobi/)

## using process
### First need to add the library

```python
pip install prioQbyrobi
```

### Then you need to import the A* Search specific queue from the library
```python
from prioQbyrobi import astar as Q

minQ = Q.PriorityQueue() #Creating an object of PriorityQueue class of the library
minQ.insert(yournodeObj) #inserting your node object into the Queue
minQ.delete() # popping your node object from the priority queue

```
## N.B: You must need to declare a variable name "total_cost" the priority is prioritized based on this
 


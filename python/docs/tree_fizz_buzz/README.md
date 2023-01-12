# Problem Description
Conduct “FizzBuzz” on a k-ary tree while traversing through it to create a new tree.
Set the values of each of the new nodes depending on the corresponding node value in the source tree.
- Write a function called fizz buzz tree
- Arguments: k-ary tree
- Return: new k-ary tree

## Whiteboard Process

![tree-breadth](/python/docs/tree_breadth_first/cc17.png)

## Approach & Efficiency

- The `breadth_first_search` approach takes in a tree as an argument and then visits every node on the same level and then once done, continues down
- The algo uses a first-in/first-out queue to hold any unvisited nodes
- with each loop, the algo removes the first item from the queue and adds it's value to the values list.
- If that node has left or right nodes, those nodes are added to the end of the queue and visited left -> right.
### Big-O 
- Time: O(n), where n is the number of nodes in the tree, because we must visit each node in the tree and get their values.
- Space: O(n), where n is the number of nodes in the tree, because we must hold all nodes in the tree once the are evaluated and return them to the user.

## API
- using the `BinaryTree` class:
  - use `breadth_first_search`
    - input: tree
    - output: list of values from each node in the tree

## Tests

- run tests using `pycharm tests/test_breadth_first.py`
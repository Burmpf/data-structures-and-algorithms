# Problem Description
Conduct “FizzBuzz” on a k-ary tree while traversing through it to create a new tree.
Set the values of each of the new nodes depending on the corresponding node value in the source tree.
- Write a function called fizz buzz tree
- Arguments: k-ary tree
- Return: new k-ary tree

## Whiteboard Process

![tree-breadth](/docs/tree_fizz_buzz/cc18.png)

## Approach & Efficiency
Clone the tree and then go through the nodes using the modify function. 
Time: O(n) because it runs through every node in the tree one at a time
Space: O(n) because its output is the new cloned/ modified tree


## Tests

- run tests using `pycharm tests/test_tree_fizz_buzz`
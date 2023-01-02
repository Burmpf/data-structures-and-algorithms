# Stacks and Queues
- Stack: a linked list where you can only add and subtract from the top. It cannont see the previous values, only the next
- Queue: similar to a stack but things are added to the end and removed from the top (generally)
## Challenge
Create both of these structures with their appropriate  methods and error handling for both

## Approach & Efficiency
- These function as following:
  - time- O(1)
  - space- O(n)
  - 
## Methods
Stack:
  - push- adds to head
  - pop- removes from top and returns value of node removed
  - peek- see value of top node
  - is_empty- returns boolean if top is not None

Queue:
  - enqueue- adds to end of list
  - dequeue- removes from top of list and returns the value the removed node
  - peek- returns top node value
  - is_empty- same as stacks


## Tests
- [queue](../tests/data_structures/test_queue.py)
- [stack](../tests/data_structures/test_stack.py)
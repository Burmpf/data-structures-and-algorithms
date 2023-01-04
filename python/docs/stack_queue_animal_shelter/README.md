# Stacks and Queues- Animal Shelter
- Stack: a linked list where you can only add and subtract from the top. It cannont see the previous values, only the next
- Queue: similar to a stack but things are added to the end and removed from the top (generally)
## Challenge
Create a class called AnimalShelter which holds only dogs and cats.
The shelter operates using a first-in, first-out approach.

## Approach & Efficiency
Dequeue
    time: O(N)
    space: O(N)
Enqueue:O(1)

## Whiteboard
[Whiteboard](whiteboard_animal_shelter.png)
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
- [Animal-Shelter](../tests/code_challenges/test_stack_queue_animal_shelter.py)

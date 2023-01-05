# Stacks and Queues- Brackets

## Challenge
Write a function called validate brackets
Arguments: string
Return: boolean
representing whether or not the brackets in the string are balanced

## Approach & Efficiency
    time: O(N)
    space: O(N)


## Whiteboard
[Whiteboard](whiteboard.png)
## Methods
multi_bracket_validation: this method takes 2 stacks of brackets, 1 open and 1 close and compares them to ensure theyre facing the correct way. If they are not it returns a False, if they are correctly facing it returns True

## Tests
- [Animal-Shelter](../tests/code_challenges/test_stack_queue_brackets.py)

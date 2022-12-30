# Challenge Summary
merge two lists, one value from list 1 then the next value from list 2... creating a "zipper" effect

## Whiteboard Process

[](linked-list-zip.png)

## Approach & Efficiency
Approach: create a pointer for each list and iterate through both. each time one goes it puts the head value from list a onto the next value of list b. list b will be erased and the leftover one, mutated. 


Efficiency: O(1): the pointers are just being rearranged, so no new memory is needed

## Solution
- pytest ./tests/code_challenges/test_linked_list_insertions.py`



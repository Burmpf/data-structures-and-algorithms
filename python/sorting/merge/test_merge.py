import pytest
from sorting.merge.merge_sort import merge_sort

def test_merge_sort():
    input_list = [12, 11, 13, 5, 6, 7]
    assert merge_sort(input_list) == [5, 6, 7, 11, 12, 13]

def test_merge_sort_empty():
    input_list = []
    assert merge_sort(input_list) == []

def test_merge_sort_one():
    input_list = [1]
    assert merge_sort(input_list) == [1]

def test_merge_sort_two():
    input_list = [2, 1]
    assert merge_sort(input_list) == [1, 2]

def test_merge_sort_three():
    input_list = [3, 2, 1]
    assert merge_sort(input_list) == [1, 2, 3]

def test_merge_sort_reverse():
    input_list = [3, 2, 1]
    assert merge_sort(input_list) == [1, 2, 3]
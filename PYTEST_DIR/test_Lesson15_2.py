from binarytree import *
from Lesson15_2for_test import Node
import pytest

@pytest.fixture
def binary_tree():
    root = Node(5)
    root.insert(3)
    root.insert(8)
    root.insert(2)
    root.insert(4)
    root.insert(7)
    root.insert(9)
    return root



def test_insert(binary_tree):
    binary_tree.insert(6)
    assert binary_tree.right.left.left.val == 6

def test_tree_min(binary_tree):
    assert binary_tree.tree_min() == 2

def test_tree_max(binary_tree):
    assert binary_tree.tree_max() == 9

def test_delete(binary_tree):
    binary_tree.delete(3)
    assert binary_tree.left.val == 4
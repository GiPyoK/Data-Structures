import sys
import os
# sys.path.append('../queue_and_stack')
sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        '../queue_and_stack'
        )
    )
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # This would be only needed if there was deleted method to BST
        # because BST is always initialized with the root.
        # check for empty root (base case)
        if self == None:
        # create a new tree with given value
            self = BinarySearchTree(value)
            return

        # compare with root
        # less than the root, move left
        if value < self.value:
            # check left
            # if left exists, move left
            if self.left:
                self.left.insert(value)
            # else, create new value and connect left to it
            else:
                self.left = BinarySearchTree(value)
                return

        # greater or equal to the root, move right
        else:
            # check right
            # if right extist, move right
            if self.right:
                self.right.insert(value)
            # else, create new value and connect right to it
            else:
                self.right = BinarySearchTree(value)
                return
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check for empty root
        if self == None:
            return False

        # if the value is the target, return true
        if target == self.value:
            return True

        # else if the value is less than the target, move left
        elif target < self.value:
            if self.left:
                return self.left.contains(target)

        # else if the value is greater than the target, move right
        else:
            if self.right:
                return self.right.contains(target)
        
        return False
        

    # Return the maximum value found in the tree
    def get_max(self):
        # go to very right of the tree
        while self.right:
            self = self.right
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self == None:
            return
        
        # call the function
        cb(self.value)

        # if left is not None, go to left
        if self.left:
            self.left.for_each(cb)

        # if right is not None, go to right
        if self.right:
            self.right.for_each(cb)



    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# insert test
bst = BinarySearchTree(5)
bst.insert(3)
bst.insert(7)
bst.insert(4)
print(bst.contains(3))
print(bst.contains(7))
print(bst.contains(4))
print(bst.contains(8))
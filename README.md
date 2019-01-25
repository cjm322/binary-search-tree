# Linked Lists vs. Sorted Arrays
## Sorted Arrays
- Insterting a new item is quite slow: O(N)
- Searching is quite fast w/ binarry search: O(log N)
- Removing an item is slow: O(N)

## Linked Lists
- Insearting a new item is very fast: O(1)
- Searching is sequential: O(N)
- Removing an item is fast because of the references: O(1)

## Conclusion
There are tradeoffs between using sorted arrays and linked lists - we must make a choice. In order to make this choice, we must know in advanced what
operation the user will use. But this is futile as users are going to have
varied needs. Therefore there is no optimal choice!

## Solution
Use a Binary search tree:
- Predictable behavior
- Very fast: O(log N))

# Trees
Trees have nodes with data and connectiom between the nodes (called edges)
- Nodes
- Edges

All nodes can be access through the the root node.
A node directly connects to another node (the child node).
Every child node has a parent node.
Every mode without a child node is a leaf node.

# Binary Search Trees
- Data structure
- Keeps the keys in sorted order: lookup and other operations
can use the principle of binary search
- Every node can have at most two children: left and right child
- left child: smaller than parent
- right child: greater than parent

Therefore, all of nodes on the left are smaller than the root node
and all of the nodes on the right are larger than the root node.

## Why is this good?
On every decision we get rid of half of the data in which we are searching!
This results in a favorable time complexity of O(logN)

# Height of the tree
This is the number of layers a tree contains
## layer 1: 1 node -> 2^0
- root: 12
## layer 2: 2 nodes -> 2^1
- left: 4
- right: 20
## layer 3: 3 nodes -> 2^2
- left: 1, 5
- right: 0, 7
## layer h
h -> 2^h-1 nodes

h is going to be porportional to O(logN) which results in a 
balanced tree. If the tree is unbalanced (asymmetric) then there
is a problem.

## Traversal
Sometimes it is neccessary to vist every node in the tree
### In-order traversal
We vist the left subtree + the root node + the right sub tree rescursively
### Pre-order traversal
We visit the root + left subtree + rightsubtree recursively
### Post-order traversal
We visit the left subtree + right subtree + the root recursively

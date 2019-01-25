from binary_search_tree import Node, BinarySearchTree
import random

bst = BinarySearchTree()
s = []

for x in range(10):
  rn = random.randint(1,1000)
  s.append(rn)
  bst.insert(rn)

print(s)
print("Min value: ", bst.getMinValue())
print("Max value: ", bst.getMaxValue())
bst.traverse()
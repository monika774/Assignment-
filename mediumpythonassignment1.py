"""Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

print("\t\tGiven a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.")
class Node:
 
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def lca(root, n1, n2):
 
    
    if root is None:
        return None
 
    if(root.data > n1 and root.data > n2):
        return lca(root.left, n1, n2)
 
    if(root.data < n1 and root.data < n2):
        return lca(root.right, n1, n2)
 
    return root
 
 
# Driver code
root = Node(6)
root.left = Node(2)
root.right = Node(8)
root.left.left = Node(0)
root.left.right = Node(4)
root.right.left = Node(7)
root.right.right = Node(9)
root.left.right.left = Node(3)
root.left.right.right = Node(5)
 
 
# Function calls
n1 = 2
n2 = 8
t = lca(root, n1, n2)
print("LCA of %d and %d is:- %d" % (n1, n2, t.data))







Input: nums = [3,2,3]
Output: [3]"""

print("/t/t Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.")
def findMajority(arr, n):
	flag = 0
	for i in range(n):
		count = 0
		for j in range(i, n):
			if (arr[i] == arr[j]):
				count+=1

		
		if (count > int(n / 3)):
			print(arr[i], end = " ")
			flag = 1
	
	if (flag == 0):
		print("No Majority Element")

arr = [ 3,2,3 ]
n = len(arr)

# Function calling
findMajority(arr, n)
 

 

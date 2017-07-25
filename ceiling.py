class Node:

	def __init__(self, item, left=None, right=None):
		self.item = item
		self.left = left
		self.right = right

class Tree:

	def __init__(self):
		self.root = None

	def recurse_add(self, ptr, item):
		if ptr == None:
			return Node(item)
		elif item < ptr.item:
			ptr.left = self.recurse_add(ptr.left, item)
		elif item > ptr.item:
			ptr.right = self.recurse_add(ptr.right, item)
		return ptr

	def add(self, item):
		self.root = self.recurse_add(self.root, item)

	def recur_shape(self, ptr, s):
		if ptr.left:
			self.recur_shape(ptr.left, s + "l")
		if ptr.right:
			self.recur_shape(ptr.right, s + "r")
		if not ptr.left and not ptr.right:
			self.s += s + "-"
		return self.s

	def shape(self):
		self.s = ""
		s = ""
		self.s += self.recur_shape(self.root, s)
		return self.s


line = [int(x) for x in input().split()]
shapes = []
for i in range(0, line[0]):
	tree = Tree()
	for n in [int(x) for x in input().split()]:
		tree.add(n)
	shapes.append(tree.shape())
shapes = set(shapes)	
print(len(shapes))

class Node:

	def __init__(self, value=None):
		self.value = value
		self.next = next

class linkedlist:

	def __init__(self):
		self.head = head
		self.current_node = current_node

	def add_node(self, value):
		if self.head == None:
			self.head = Node(value)
			self.current_node = self.head
			return

	def delete_node(self, value):
		prev = None
		found = False
		current_node = self.current_node

		while not found:
			if current_node.value == value:
				found = True
			else:
				prev = current_node.value
				current_node = current_node.next

	def print_list(self):
		current_node = self.current_node
		while self.current_node != None:
			print self.current_node.value
			current_node = current_node.next

	def length(self):
		current_node = self.current_node
		count = 0
		while self.current_node != None:
			count += 1
			current_node = current_node.next

		return count

test = linkedlist()
test.add_node(30)
test.add_node(15)
test.add_node(45)
test.print_list()
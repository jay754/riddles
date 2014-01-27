class Node:

	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

class linkedlist:

	def __init__(self):
		self.head = None

	def add_node(self, value):
		if self.head == None:
			self.head = Node(value)
		else:
			self.head.next = Node(value)

	def delete_node(self, value):
		#a bit broken
		prev = None
		found = False
		current_node = self.head

		while not found:
			if current_node.value == value:
				found = True
				current_node.value = None
			else:
				prev = current_node.value
				current_node = current_node.next

	def print_list(self):
		current_node = self.head
		while current_node != None:
			print current_node.value
			current_node = current_node.next

	def length(self):
		current_node = self.head
		count = 0
		while current_node != None:
			count += 1
			current_node = current_node.next

		return count

if __name__ == '__main__':

	test = linkedlist()
	test.add_node(30)
	test.add_node(45)
	test.add_node(16)
	test.print_list()
	print test.length()
	test.delete_node(30)
	test.print_list()
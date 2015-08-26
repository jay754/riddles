class Node:

	def __init__(self, value=None, next=None):
		self.value = value
		self.next = next

class Linkedlist:

	def __init__(self, head=None):
		self.head = head

	def add_node(self, value):
		new_node = Node(value)
		new_node.next = self.head
		self.head = new_node

	def delete_node(self, value):
		prev = None
		found = False
		current_node = self.head

		while found:
			if current_node.value == value:
				found = True
			else:
				prev = current_node
				current_node = current_node.next

	def length(self):
		current_node = self.head
		count = 0
		while current_node != None:
			count += 1
			current_node = current_node.next

		return count

	def get_position(self, value):
		count = 1
		found = False
		current_node = self.head

		while not found:
			if current_node.value == value:
				found = True
				print count
			else:
				current_node = current_node.next
				count += 1

#testing

test = Linkedlist()
test.add_node(30) #points to None which the value will equal to and end the while loop
test.add_node(29) #points to 30
test.add_node(25) #points to 29
test.add_node(16) #points to 25

print test.length()

test.delete_node(29)

print test.length()

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
		current_node = self.head
		prev = None
		found = False

		while found is False:
			if current_node.value == value:
				found = True
			else:
				prev = current_node
				current_node = current_node.next

		if prev == None:
			self.head = current_node.next
		else:
			prev.next = current_node.next

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

	def display(self):
		current_node = self.head

		while current_node != None:
			print current_node.value
			current_node = current_node.next

	def is_palindrome(self):
		#2.7
		current_node = self.head
		word = ""

		while current_node != None:
			word += current_node.value
			current_node = current_node.next

		if word == word[::-1]:
			return True

		return False

	def delete_middle_node(self):
		#2.4
		current_node = self.head
		l = self.length()
		mid = l/2
		prev = None
		count = 0
		found = False

		while found is False:
			if count == mid:
				found = True
			else:
				prev = current_node
				current_node = current_node.next
				count += 1

		if prev == None:
			self.head = current_node.next
		else:
			prev.next = current_node.next

#testing

test = Linkedlist()
test.add_node('j')
test.add_node('b') #points to 30
test.add_node('o') #points to 29
test.add_node('b') #points to 25 [16, 25, 29, 30]
test.add_node('j')

# print test.is_palindrome()

test.delete_middle_node()
test.display()

# test.delete_node(29)

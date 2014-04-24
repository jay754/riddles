"""Stack ADT.

LIFO

Operations:
	pop: remove and return top item
    push(item): store item on top of stack
    is_empty?: return whether stack is empty.
    peek: returns the last element implemneted in the stack
"""

class Stack
  # a getter for data
  attr_accessor :data

  def initialize
    @data = []
  end

  def pop
    @data.pop()
  end

  def is_empty?
    @data.empty?
  end

  def push(o)
    @data.push(o)
  end

  def peek
    @data.last
  end

end

s = Stack.new()
s.push(2) #[2]
s.push(4) #[2, 4]
s.pop #[2]
s.push(5) #[2,5]
puts s.peek  #[5]

puts s.data #[2,5]

puts s.is_empty?
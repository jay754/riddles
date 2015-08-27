#FIFO

class Queue:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.insert(0, value)
        #for inserting at the first element instead of append which pushes towards the end

    def pop(self):
        self.data.pop()

    def size(self):
        return len(self.data)

    def display(self):
        print self.data

q = Queue()

q.push(2) #[2]
q.push(3) #[3, 2]
q.push(1) #[1,3,2]

q.display()

q.pop()

q.display()

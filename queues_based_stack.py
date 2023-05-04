

class Queue:
    def __init__(self):
        self.inboud_stack = []
        self.outboud_stack = []

    def enqueue(self, data):
        self.inboud_stack.append(data)


    def dequeue(self):
        if not self.outboud_stack:
            while self.inboud_stack:
                self.outboud_stack.append(self.inboud_stack.pop())

        # return self.outboud_stack.pop()
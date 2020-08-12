class Deque:
    def __init__(self):
        self.list1 = []

    def is_empty(self):
        return self._len() == 0

    def enqstart(self, e):
        self.list1.append(e)

    def enqend(self, e):
        self.list1.insert(0, e)


    def deqstart(self):
        del self.list1[-1]

    def deqend(self):
        del self.list1[0]

    def _len(self):
        return len(self.list1)

    def Start(self):
        return self.list1[-1]

    def End(self):
        return self.list1[0]


    def show_data(self):
        return self.list1

d = Deque()
d.enqstart(5)
d.enqend(7)
print(d.show_data())

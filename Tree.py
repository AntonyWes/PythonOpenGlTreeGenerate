class Tree:

    def __init__(self, data, leaves):
        self.data = data
        self.leaves = []
        self.x = 0
        self.y = 0
        if leaves:
            for item in leaves:
                if item:
                    self.leaves.append(Tree(**item))

    def get_elements(self, stage):
        res = [(stage, self)]
        if self.leaves:
            for item in self.leaves:
                res.extend(item.get_elements(stage + 1))
        return res

    def getLines(self):
        res = []
        if self.leaves:
            for item in self.leaves:
                res.append((self.x, self.y, item.x, item.y))
                res.extend(item.getLines())
        return res



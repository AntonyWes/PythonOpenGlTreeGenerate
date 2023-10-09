class Tree:

    def __init__(self, data, leaves):
        self.data = data
        self.leaves = []
        if leaves:
            for item in leaves:
                if item:
                    self.leaves.append(Tree(**item))

    def get_elements(self, stage):
        res = [(stage, self.data)]
        if self.leaves:
            for item in self.leaves:
                res.extend(item.get_elements(stage + 1))
        return res



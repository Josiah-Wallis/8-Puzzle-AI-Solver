class queue:                                                    # Queue with sorted append
    def __init__(self):
        self.line = []

    def append(self, node, f = None):                           # Input: node: SNode, f: list containing evaluation function and problem
        if f is None:
            self.line.append(node)
        else:
            self.line.append(node)
            self.line.sort(key = lambda x: f[0](x, f[1]))       # Sort based on evaluation function output

    def pop(self):
        return self.line.pop(0)

    def empty(self):
        return True if len(self.line) == 0 else False

    def top(self):
        return self.line[0]

    def size(self):
        return len(self.line)

class SNode:                                                    # State Node
    def __init__(self, state):
        self.STATE = state                                      # 3x3 list representing puzzle state
        self.PARENT = None                                      # Pointer to puzzle state before self.STATE
        self.ACTION = None                                      # Operator applied to parent to obtain self.STATE
        self.PATH_COST = 0                                      # Number of edges from initial state to self.STATE

    def __eq__(self, other):
        return self.STATE == other.STATE

    def __contains__(self, item):
        for x in item:
            if self == x:
                return True
        return False

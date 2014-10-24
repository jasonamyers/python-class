class Node(object):

    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []
        self.depth = []

    def __iter__(self):
        return self.children.__iter__()

    def __repr__(self):
        return "Node (%r)" % self.value

    def add_child(self, other_node):
        self.children.append(other_node)
        other_node.parent = self

    def depth_first(self):
        self.depth.append(child)
        for child in self.children:
            child.depth_first()

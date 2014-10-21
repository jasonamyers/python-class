# node.py

class Node(object):
    def __init__(self,value):
        self.value = value
        self.parent = None
        self.children = []

    def __repr__(self):
        return "Node(%r)" % self.value

    def __iter__(self):
        return iter(self.children)

    def add_child(self,other_node):
        self.children.append(other_node)
        other_node.parent = self

# Sample code to test
if __name__ == '__main__':
    root = Node(0)
    root.add_child(Node(1))
    root.add_child(Node(2))
    root.add_child(Node(3))

    print("Children of", root)
    for child in root:
        print(child)

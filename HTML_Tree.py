from HTMLTag import HTMLTag


class Node:

    def __init__(self, tag, is_closed):
        self.tag = tag
        self.is_closed = is_closed
        self.is_child = False

    def close(self):
        if not self.is_closed:
            self.is_closed = True


class HTMLTree:

    def __init__(self):
        self.tree = []

    def __str__(self):
        return ''.join(str(x.tag) for x in self.tree if not x.is_child)

    def get_html(self):
        return [x for x in self.tree if not x.is_child]

    def add_node(self, node):
        parent_node = self.backward()
        if parent_node:
            node.is_child = True
            parent_node.tag.append_child(node.tag)
        self.tree.append(node)

    def add_attribute(self, key, value):
        if len(self.tree) > 0:
            node = self.tree[-1]
            node.tag.add_attribute(key, value)

    def set_value(self, value):
        if len(self.tree) > 0:
            node = self.tree[-1]
            node.tag.value = value

    def close_node(self):
        node = self.backward()
        if node:
            node.close()

    def backward(self):
        for x in self.tree[::-1]:
            if not x.is_closed:
                return x

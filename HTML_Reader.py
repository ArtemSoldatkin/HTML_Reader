from HTMLTag import HTMLTag
from HTML_Tree import HTMLTree, Node


class HTMLReader:

    def __init__(self, html):
        self.html = html
        self.pos = 0
        self.isQuot = False
        self.isValue = False
        self.html_tags = []
        self.tree = HTMLTree()
        self.tag = self.get_tag()

    def __str__(self):
        return str(self.tree)

    def get_tag(self):
        tag = ""
        for char in self.html[self.pos:]:
            self.pos += 1
            if self.isValue:
                if char != "<":
                    tag += char
                    continue
                else:
                    self.pos -= 1
                    return tag

            if char == ">":
                return char
            if char == '<':
                if tag:
                    self.pos -= 1
                    return tag
                return char
            if char == '"' or char == "'":
                self.isQuot = not self.isQuot
                if not self.isQuot:
                    return tag
                continue
            if not self.isQuot:
                if char == "/":
                    return char
                if char == " " or char == "=":
                    if tag:
                        return tag
                    continue
            tag += char
        return tag

    def read(self):
        while self.pos < len(self.html):
            if self.tag == '<':
                tag = self.get_tag()
                self.isValue = False
                if tag != '/':
                    new_tag = HTMLTag(tag)
                    self.tree.add_node(Node(new_tag, False))
                else:
                    self.tree.close_node()
            elif self.tag == '/':
                tag = self.get_tag()
                if tag == '>':
                    self.tree.close_node()
            elif self.tag == '>':
                self.isValue = True
                tag = self.get_tag()
                if tag != '<':
                    self.tree.set_value(tag)
                    self.isValue = False
                else:
                    self.isValue = False
                    continue

            elif not self.isValue:
                self.tree.add_attribute(self.tag, self.get_tag())
            self.tag = self.get_tag()


def main():

    html = '<div class="test_cls">div text<span class="span_cls">span text<input type="text" /> <button class="button_cls">button text</button></span></div><div class="second_div">div textx <p class="p_cls">text</p><div class="p2">new text</div></div>'

    reader = HTMLReader(html)
    reader.read()
    print(reader)


main()

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

    def get_tag(self):
        tag = ""
        for char in self.html[self.pos:]:
            self.pos += 1
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

    def read_2(self):
        while self.pos < len(self.html):
            if self.tag == '<':
                tag = self.get_tag()
                print("TAG", self.tag, tag)
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
                    self.isValue = False
            elif self.tag == '>':
                self.isValue = True
            elif not self.isValue:
                self.tree.add_attribute(self.tag, self.get_tag())
            elif self.isValue:
                self.tree.set_value(self.tag)
            self.tag = self.get_tag()
    '''
    def get_tag(self):
        tag = ""
        for char in self.html[self.pos:]:
            self.pos += 1
            if (not self.isValue and char == "<") or char == ">":
                return char
            elif self.isValue and char == '<':
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
                if tag != '/':
                    new_tag = HTMLTag(tag)
                    if self.isValue:
                        if self.html_tags[-1]:
                            self.html_tags[-1].append_child(new_tag)
                            self.isValue = False
                    self.html_tags.append(new_tag)
                else:
                    self.isValue = False
            elif self.tag == '/':
                tag = self.get_tag()
                if tag == '>':
                    pass
            elif self.tag == '>':
                self.isValue = True
            elif not self.isValue and len(self.html_tags) > 0:
                self.html_tags[-1].add_attribute(self.tag, self.get_tag())
            elif self.isValue:
                self.html_tags[-1].value = self.tag
            self.tag = self.get_tag()

    def __str__(self):
        return "".join(str(x) for x in self.html_tags)
    '''


def main():
    '''
    html = '<input type="text" class="two classes" value="some value" placeholder="some placeholder"/>'
    '''
    html = '<div class="test_cls"><span class="span_cls"><button class="button_cls"></button></span></div><div class="second_div"><p class="p_cls"></p></div>'

    reader = HTMLReader(html)
    '''
    reader.read()
    print(reader)
    '''
    reader.read_2()
    print(reader.tree)


main()

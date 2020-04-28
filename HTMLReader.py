from HTMLTag import HTMLTag
from HTMLTree import HTMLTree, Node


class HTMLReader:

    def __init__(self, html):
        self._html = html
        self._pos = 0
        self._is_quot = False
        self._is_value = False
        self._html_tags = []
        self._tree = HTMLTree()
        self._tag = self._get_tag()

    def __str__(self):
        return str(self._tree)

    def _get_tag(self):
        tag = ""
        for char in self._html[self._pos:]:
            self._pos += 1
            if self._is_value:
                if char != "<":
                    tag += char
                    continue
                else:
                    self._pos -= 1
                    return tag
            if char == ">":
                return char
            if char == '<':
                if tag:
                    self._pos -= 1
                    return tag
                return char
            if char == '"' or char == "'":
                self._is_quot = not self._is_quot
                if not self._is_quot:
                    return tag
                continue
            if not self._is_quot:
                if char == "/":
                    return char
                if char == " " or char == "=":
                    if tag:
                        return tag
                    continue
            tag += char
        return tag

    def read(self):
        while self._pos < len(self._html):
            if self._tag == '<':
                tag = self._get_tag()
                self._is_value = False
                if tag != '/':
                    new_tag = HTMLTag(tag)
                    self._tree.add_node(Node(new_tag, False))
                else:
                    self._tree.close_node()
            elif self._tag == '/':
                tag = self._get_tag()
                if tag == '>':
                    self._tree.close_node()
            elif self._tag == '>':
                self._is_value = True
                tag = self._get_tag()
                if tag != '<':
                    self._tree.set_value(tag)
                    self._is_value = False
                else:
                    self._is_value = False
                    continue
            elif not self._is_value:
                self._tree.add_attribute(self._tag, self._get_tag())
            self._tag = self._get_tag()


def main():

    html = '<div class="test_cls">div text<span class="span_cls">span text<input type="text" /> <button class="button_cls">button text</button></span></div><div class="second_div">div textx <p class="p_cls">text</p><div class="p2">new text</div></div>'

    reader = HTMLReader(html)
    reader.read()
    print(reader)


main()

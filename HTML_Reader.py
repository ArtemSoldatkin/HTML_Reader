from HTMLTag import HTMLTag


class HTMLReader:

    def __init__(self, html):
        self.html = html
        self.pos = 0
        self.tag = ""
        self.isQuot = False
        self.isValue = False
        self.html_tags = []

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
                    self.html_tags.append(HTMLTag(tag))
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


def main():
    '''
    html = '<input type="text" class="two classes" value="some value" placeholder="some placeholder"/>'
    '''
    html = '<div class="test">value <input type="text" /></div>'

    reader = HTMLReader(html)
    reader.read()
    print(reader)


main()

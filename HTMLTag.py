class HTMLTag:
	
	def __init__(self, name):
		self.name = name
		self.attribute = {}
		self.value = ""
		self.children = []
		
	def add_attribute(self, key, value):
		self.attribute[key] = value

	def add_child(self, child):
		self.children.append(child)	

	def attr_to_str(self):
		return " ".join([f'{k}="{v}"' for k,v in self.attribute.items()])
		
	def __str__(self):
		if self.name == "input":
			return f"<{self.name} {self.attr_to_str()}/>"
		else:
			return f"<{self.name} {self.attr_to_str()}>{self.value}</{self.name}>"

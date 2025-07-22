from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.children is None or len(self.children) == 0:
            raise ValueError("Parents need children")
        elif self.tag is None:
            raise ValueError("Tags are required to nest values")
        else:
            ret = f"<{self.tag}{self.props_to_html()}>"
            for child in self.children:
                ret += child.to_html()
            ret += f"</{self.tag}>"

            return ret
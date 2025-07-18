
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        return NotImplemented
    
    def props_to_html(self):
        "".join(list(map(format_props, self.props)))

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"
    
def format_props(key, value):
    return f' {key}="{value}"'
        
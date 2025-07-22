
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        return "".join(list(map(lambda prop: format_props(prop[0], prop[1]), self.props.items()))) if self.props is not None else ""

    def __eq__(self, value):
        return self.tag == value.tag and self.value == value.value and self.children == value.children and self.props == value.props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html() if self.props is not None else None})"
    
def format_props(key, value):
    return f' {key}="{value}"'
        
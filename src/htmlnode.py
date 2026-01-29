# Class will represent a "node" in an HTML document tree
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError("to_html not implemented")
    
    # Returns a string containing props
    def props_to_html(self):
        if self.props:
            props = self.props
            result = ""
            for key in props:
                result += f' {key}="{props[key]}"'
            return result
        else:
            return ""
        
    # We use this for checking object properties
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
    # We use this for tests
    def __eq__(self, other):
        if self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props:
            return True
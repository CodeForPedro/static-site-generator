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
        
# Class represents a single HTML tag with no children
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("all leaf nodes must have a value")
            return
        if self.tag == None:
            return f"{self.value}"
        return f"<{self.tag}>{self.value}</{self.tag}>"
            
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"

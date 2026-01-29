import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "Anchor text", None, {"target":"link to website", "target2": "link to person"})
        node2 = HTMLNode("a", "Anchor text", None, {"target":"link to website"})
        self.assertEqual(repr(node), "HTMLNode(tag=a, value=Anchor text, children=None, props={'target': 'link to website', 'target2': 'link to person'})")
        self.assertNotEqual(node, node2)
        self.assertEqual(node.props_to_html(), ' target="link to website" target2="link to person"')

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_eq(self):
        node = LeafNode("h1", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<h1>This is a paragraph of text.</h1>")





if __name__ == "__main__":
    unittest.main()
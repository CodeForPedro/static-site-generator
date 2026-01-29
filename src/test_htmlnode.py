import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "Anchor text", None, {"target":"link to website", "target2": "link to person"})
        node2 = HTMLNode("a", "Anchor text", None, {"target":"link to website"})
        self.assertEqual(repr(node), "HTMLNode(tag=a, value=Anchor text, children=None, props={'target': 'link to website', 'target2': 'link to person'})")
        self.assertNotEqual(node, node2)
        self.assertEqual(node.props_to_html(), ' target="link to website" target2="link to person"')

if __name__ == "__main__":
    unittest.main()
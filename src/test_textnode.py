import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALIC)
        node4 = TextNode("This is a", TextType.BOLD)
        node5 = TextNode("This is an image of a cat", TextType.IMAGE, "sample link")
        node6 = TextNode("This is an image of a cat", TextType.IMAGE, "sample")
        self.assertEqual(node, node2)
        self.assertNotEqual(node2, node3)
        self.assertNotEqual(node3, node4)
        self.assertNotEqual(node5, node6)

if __name__ == "__main__":
    unittest.main()
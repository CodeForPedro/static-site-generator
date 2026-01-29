from textnode import TextNode, TextType

def main():

    Node = TextNode("Test", TextType.LINK, "https://docs.python.org/3/tutorial/classes.html")
    print(Node)

main()
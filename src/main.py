
from htmlnode import HTMLNode

def main():

    node = HTMLNode("a", "Anchor text", None, {"target":"link to website", "target2": "link to person"})
    print(repr(node))


main()
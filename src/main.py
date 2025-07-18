from textnode import TextNode, TextType

def main():
    node = TextNode("test", TextType.LINK, "www.test.co")
    print(node)

main()
import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def testtesting(self):
        node = ParentNode("p", [LeafNode("b", "Bold text"), LeafNode(None, "Normal text"), LeafNode("i", "italic text")])
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i></p>")

    def test_to_html_with_grandchildren_and_uncle(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        uncle_node = LeafNode("a", "Test", props={"href":"www.google.com", "target":"_blank"})
        parent_node = ParentNode("div", [child_node, uncle_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span><a href=\"www.google.com\" target=\"_blank\">Test</a></div>")

if __name__ == "__main__":
    unittest.main()
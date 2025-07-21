import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def testNone(self):
        node1 = HTMLNode()
        self.assertIsNone(node1.children)
        self.assertIsNone(node1.props)
        self.assertIsNone(node1.value)
        self.assertIsNone(node1.tag)
    
    def testEq(self):
        node1 = HTMLNode("a", "Test", props={"href":"www.google.com", "target":"_blank"})
        node2 = HTMLNode("a", "Test", props={"href":"www.google.com", "target":"_blank"})
        self.assertEqual(node1, node2)
    
    def testPropsPrintCorrectly(self):
        children = [HTMLNode(value="Test")]
        node1 = HTMLNode("a", "Test", children, {"href":"www.google.com", "target":"_blank"})
        self.assertIn('href="www.google.com" target="_blank"', repr(node1))
        pass
    
if __name__ == "__main__":
    unittest.main()
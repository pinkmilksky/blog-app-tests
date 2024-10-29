from unittest import TestCase
from blog import Blog


class TestBlog(TestCase):
    def test_create_blog(self):
        b = Blog("Test", "Test Author")

        self.assertEqual("Test", b.title)
        self.assertEqual("Test Author", b.author)
        self.assertListEqual([], b.posts)
        self.assertEqual(0, len(b.posts))


    def test_repr(self):
        b = Blog("Test", "Test Author")

        self.assertEqual(b.__repr__(), "Test by Test Author (0 posts)")


    def test_repr_multiple_posts(self):
        b = Blog("Test", "Test Author")
        b.posts = ["Test1", "Test2"]

        self.assertEqual(b.__repr__(), "Test by Test Author (2 posts)")







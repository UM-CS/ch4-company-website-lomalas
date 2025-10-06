from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test")

    def test_template_name_correct(self):
        response = self.client.get(reverse("post_list"))
        self.assertTemplateUsed(response, "post_list.html")

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.user = User.objects.create_user(
            username="testuser", password="secret"
        )
        cls.post = Post.objects.create(
            title="Test Title",
            author=cls.user,
            body="This is a test",
        )

    def test_model_content(self):
        self.assertEqual(self.post.body, "This is a test")
        self.assertEqual(self.post.title, "Test Title")
        self.assertEqual(str(self.post.author), "testuser")

    def test_template_name_correct(self):
        response = self.client.get(reverse("post_list"))
        self.assertTemplateUsed(response, "post_list.html")

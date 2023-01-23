import sys
from django.test import TestCase
from django.urls import reverse

from .models import Post

class PostTetst(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.post = Post.objects.create(text="This is a test!")
    #sys.stderr.write(repr(object_to_print) + '\n')
    sys.stderr.write("setup done!\n")

  def test_model_content(self):
    self.assertEqual(self.post.text, "This is a test!")

  def test_url_exists_at_correct_location(self):
    response = self.client.get("/") # in module range!
    self.assertEqual(response.status_code, 200)

  def test_url_available_by_name(self):
    response = self.client.get(reverse("listika"))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "listika.html")
    self.assertContains(response, "This is a test!")

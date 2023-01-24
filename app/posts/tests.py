# K6ik on h2kk... peaasi et $$ tuleb
# ma ei oska midagi tegelt
# Aga palgake finbitest Pavel Sevakin, see vend teeb JAVA + SQL
import sys
from django.test import TestCase
from django.urls import reverse

from .models import Post

class PostTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    cls.post = Post.objects.create(text="This is a test!")
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
    #sys.stderr.write("K6ik testid tehtud. t88tab\n")
    #sys.stderr.write(repr(object_to_print) + '\n')

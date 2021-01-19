from django.urls import reverse
from django.urls import resolve
from django.test import TestCase
from django.contrib.auth.models import User
from .views import home
from .models import familyevent

class HomeTests(TestCase):
  def setup(self):
    self.familyevent = familyevent.objects.create(name='xxx',description='xxx')
    url = reverse('home')
    self.response = self.client.get(url)

  def test_home_view_status_code(self):
    self.assertEquals(self.response.status_code, 200)
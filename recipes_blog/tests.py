# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from models import Post


# Create your tests here

class PostTests(TestCase):

    def test_str(self):
        test_title = Post(title="my first blog")
        self.assertEqual(str(test_title),'my first blog')
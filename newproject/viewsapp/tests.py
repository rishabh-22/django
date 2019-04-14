from django.test import TestCase
from django.http import HttpResponse
from .views import second
from  django.test.client import RequestFactory
import unittest

# Create your tests here.

class TestGreeting(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_one(self):
        """pass the test"""
        request = self.factory.get('')
        response = second(request, 11)
        self.assertEqual(response, 'Good morning!') 

    def test_two(self):
        """pass the test"""
        request = self.factory.get('')
        response = second(request, 17)
        self.assertEqual(response, 'Good afternoon')

    def test_three(self):
        """pass the test"""
        request = self.factory.get('')
        response = second(request, 20)
        self.assertNotEqual(response, "Good night")

    def test_four(self):
        """Supposed to fail"""
        request = self.factory.get('')
        response = second(request, 5)
        self.assertEqual(response, "Good night")



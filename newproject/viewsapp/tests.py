from django.test import TestCase
from django.http import HttpResponse
from .views import second, methodForTest
from  django.test.client import RequestFactory
import unittest

# Create your tests here.

class TestGreeting(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_one(self):
        """pass the test"""
        request = self.factory.get('')
        response = methodForTest(request, 11)
        self.assertEqual(response, 'Good morning!') 

    def test_two(self):
        """pass the test"""
        request = self.factory.get('')
        response = methodForTest(request, 17)
        self.assertEqual(response, 'Good afternoon')

    def test_three(self):
        """pass the test"""
        request = self.factory.get('')
        response = methodForTest(request, 20)
        self.assertEqual(response, "Good night")

    def test_four(self):
        """pass the test"""
        request = self.factory.get('')
        response = methodForTest(request, 5)
        self.assertEqual(response, "Go to bed")

    def test_five(self):
        """fail the test"""
        request = self.factory.get('')
        response = methodForTest(request, 15)
        self.assertNotEqual(response, "bye")

    def test_six(self):
        """fail the test"""
        request = self.factory.get('')
        response = methodForTest(request, 8)
        self.assertNotEqual(response, "hello")

    def test_seven(self):
        """fail the test"""
        request = self.factory.get('')
        response = methodForTest(request, 11)
        self.assertNotEqual(response, "Good morningg")

    def test_eight(self):
        """fail the test"""
        request = self.factory.get('')
        response = methodForTest(request, 5)
        self.assertNotEqual(response, "Go home")



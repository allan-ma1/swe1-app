from django.test import TestCase


class BasicTest(TestCase):
    def test_basic_math(self):
        """Test that 1 + 1 = 2"""
        self.assertEqual(1 + 1, 2)

from unittest import TestCase
from currency import convert_currency

class TestCurrencyConvertor(TestCase):

    def test_currency_conversion(self):
        """Test from INR to USD"""
        self.assertEqual(convert_currency("INR","USD").get('USD'),0.0118513524)
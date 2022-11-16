import unittest
from unittest.mock import Mock
from src.TraderBot import TraderBot


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.trader_bot = TraderBot()

    def test_get_current_price(self):
        self.assertGreater(self.trader_bot.get_current_price(), TraderBot.price_generator_bounds[0] - 1)
        self.assertLess(self.trader_bot.get_current_price(), TraderBot.price_generator_bounds[1] + 1)

    def test_post_order(self):
        order = self.trader_bot.generate_order("buy")
        credentials = Mock()

        self.assertEqual(self.trader_bot.post_order(order, credentials)['status'], "Ok")


if __name__ == "__main__":
    unittest.main()

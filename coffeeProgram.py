import unittest

from coffeeMenu import CoffeeMenu


class TestCoffeeMenu(unittest.TestCase):
  def setUp(self):
      self.menu = CoffeeMenu()

  def tearDown(self):
      self.menu = None

  def test_get_price_existing_item(self):
      self.assertEqual(self.menu.get_price('Latte'), 2.75)

  def test_get_price_non_existing_item(self):
      self.assertIsNone(self.menu.get_price('Mocha'))

  def test_add_item(self):
      self.menu.add_item('Mocha', 2.75)
      self.assertEqual(self.menu.get_price('Mocha'), 2.75)

if __name__ == '__main__':
    unittest.main()
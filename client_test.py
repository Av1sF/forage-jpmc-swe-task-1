import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    # stock, bid_price, ask_price, price
    # price = (bid_price + ask_price) / 2
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),
                       (quote['stock'],
                        quote['top_bid']['price'],
                        quote['top_ask']['price'],
                        ((quote['top_bid']['price'] + quote['top_ask']['price']) / 2)))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),
                       (quote['stock'],
                        quote['top_bid']['price'],
                        quote['top_ask']['price'],
                        ((quote['top_bid']['price'] + quote['top_ask']['price']) / 2)))

  def test_getRatio_normal(self):
    self.assertEqual(getRatio(323.432532, 3423.49045), (323.432532 / 3423.49045))

  def test_getRatio_boundary(self):
    self.assertEqual(getRatio(354423.324, 0),)
    self.assertEqual(getRatio(0, 45421.451), 0)



if __name__ == '__main__':
    unittest.main()

import unittest
from cashmashine import Bill

class TestBill(unittest.TestCase):
	def test_bill_init(self):
		b = Bill(5)
		self.assertEqual(b, 5)
	def test_bill_str(self):
		b = Bill(5)
		self.assertEqual(str(b), "a 5$ bill")


if __name__ == "__main__":
	unittest.main()

#Testovete ne trqbva da zavisqt edin ot drug!
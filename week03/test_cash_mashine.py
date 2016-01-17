import unittest
from cash_mashine import Bill, BillBatch

class TestBill(unittest.TestCase):
	def setUp(self):
		self.bill = Bill(5)

	def test_bill_init(self):
		self.assertEqual(self.bill.bill, 5)

	def test_bill_str(self):
		self.assertEqual(str(self.bill), "A 5$ bill")

	def test_bill_str(self):
		self.assertEqual(int(self.bill), 5)

	def test_bill_eq(self):
		bill2 = Bill(10)
		bill3 = Bill(5)
		self.assertNotEqual(self.bill, bill2)
		self.assertEqual(self.bill, bill3)

class TestBillBatch(unittest.TestCase):
	def setUp(self):
		self.bills = Bill(5)
		values = [10, 20, 50, 100]
		billss = [Bill(value) for value in values]
		self.batch = BillBatch(billss)


	def test_billbatch_str(self):
		self.assertEqual(str(self.bills), "a 5$ bill")

	def test_billbatch_iteration(self):
		test = []
		for bill in self.batch:
		    test.append(bill)
		test2 = "A 10$ bill", "A 20$ bill", "A 50$ bill", "A 100$ bill"
		self.assertEqual(str(test, test2)

	def test_billbatch_total(self):
		self.assertEqual(self.batch.total, 180)


if __name__ == "__main__":
	unittest.main()
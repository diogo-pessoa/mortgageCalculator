from unittest import TestCase

from cost_of_living_calculator.HouseSale import HouseSale


class TestHouseSale(TestCase):

    def setUp(self):
        print(f"Running test: {self._testMethodName}")
        sale_price = 470000
        real_state_agent_commission_rate = 0.01
        sales_costs = 5000
        self.house_sale = HouseSale(sale_price, real_state_agent_commission_rate,
                                    sales_costs)

    def test_get_return_from_sale(self):
        self.assertEqual(460300, self.house_sale.get_return_from_sale())

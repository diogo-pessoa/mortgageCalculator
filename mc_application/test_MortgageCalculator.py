from unittest import TestCase

from cost_of_living_calculator.MortgageCalculator import MortgageCalculator


class TestMortgageCalculator(TestCase):

    def setUp(self):
        print(f"Running test: {self._testMethodName}")

        house_price = 365000
        self.mortgage_cost = MortgageCalculator(house_price)
        self.mortgage_cost.subtract_early_repayment(30000)

    def test_get_monthly_payment(self):
        print(f"monthly repayment: {self.mortgage_cost.get_monthly_payment()}")
        self.assertEqual(1298, self.mortgage_cost.get_monthly_payment())

    def test_get_total_lent(self):
        print(f"Total lent: {self.mortgage_cost.get_total_lent()}")
        self.assertEqual(467280, self.mortgage_cost.get_total_lent())

    def test_get_total_interest(self):
        print(f"Total interest: {self.mortgage_cost.get_total_interest()}")
        self.assertEqual(138780, self.mortgage_cost.get_total_interest())

    def test_get_total_repayable(self):
        print(f"Total lent: {self.mortgage_cost.get_total_repayable()}")
        self.assertEqual(467280, self.mortgage_cost.get_total_repayable())

    def test_get_monthly_rate(self):
        print(f"Monthly interest rate: "
              f"{self.mortgage_cost.get_monthly_rate_percentage()}")
        self.assertEqual(0.0020833333333333333,
                         self.mortgage_cost.get_monthly_rate_percentage())

    def test_get_monthly_rate_charge(self):
        print(f"Monthly interest rate charge: "
              f"{self.mortgage_cost.get_monthly_rate_charge()}")
        self.assertEqual(684, self.mortgage_cost.get_monthly_rate_charge())

    def test_get_interest_rate_cost_monthly(self):
        print(f"Interest rate cost monthly: "
              f"{self.mortgage_cost.get_interest_rate_cost_monthly()}")
        self.assertEqual(614, self.mortgage_cost.get_interest_rate_cost_monthly())

    def test_debt_left_after_paid_years(self):
        self.assertEqual(self.mortgage_cost.get_debt_left_after_years(5), 279234)
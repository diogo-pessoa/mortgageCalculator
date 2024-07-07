from unittest import TestCase

from cost_of_living_calculator.HouseBuyMortgageCostCalculator import HouseBuyMortgageCostCalculator


class TestMortgageCost(TestCase):
    def setUp(self):
        print(f"Running test: {self._testMethodName}")
        house_buy_other_costs = 7_000
        mortgage_renegotiation_fee = 3_600
        renovation_costs = 75_000
        admin_fees = 1100
        vlt_cost_per_year = 487
        number_of_years_paid = 5
        house_price = 365_000
        monthly_repayment = 1298
        self.mortgage_cost = (
            HouseBuyMortgageCostCalculator(house_price, mortgage_renegotiation_fee, house_buy_other_costs,
                                           renovation_costs, admin_fees, number_of_years_paid, vlt_cost_per_year,
                                           monthly_repayment))

    def test_get_total_cost_per_year(self):
        print(self.mortgage_cost)
        self.assertEqual(self.mortgage_cost.get_total_cost_per_year(), 41_583)

    def test_total_cost_of_living(self):
        self.assertEqual(self.mortgage_cost.get_total_cost_living_in_mortgage(), 207_915)
